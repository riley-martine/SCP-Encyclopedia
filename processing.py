"""Remove crap from pages and change image location"""

import os
import glob
from bs4 import BeautifulSoup


def abs_paths_to_rel():
    """Change image location to local"""
    files = glob.glob(os.path.join(os.getcwd(), "html_files", "*.htm"))

    for file in files:
        print(file)

        soup = BeautifulSoup(open(file, encoding="utf8"))

        # Make the title an anchor, for the table of contents
        title = soup.find("div", id="page-title").string
        a_name = soup.new_tag("a")
        a_name['name'] = title.strip()
        soup.find("div", id="page-title").string.wrap(a_name)

        for img_tag in soup.find_all('img'):
            if(img_tag['src'].find('\"') is not -1):
                print("Found double-quote")
                img_tag['src'] = img_tag['src'].replace('\"', '')

            img_tag['src'] = '../encyclopedia/' + \
                os.path.basename(img_tag['src'])
            print(img_tag['src'])

        write_out = open(file, 'w', encoding="utf8")
        write_out.write(str(soup))

    series1_contents = BeautifulSoup(open(os.path.join(
        "html_files", "scp-series-contents.html"), encoding="utf8"))

    lis = series1_contents.find_all("li")
    for li in lis:
        a = li.find("a")
        a['href'] = a['href'].replace('/', '#')
        a['href'] = a['href'].upper()

    series2_contents = BeautifulSoup(open(os.path.join(
        "html_files", "scp-series2-contents.html"), encoding="utf8"))

    lis = series1_contents.find_all("li")
    for li in lis:
        a = li.find("a")
        a['href'] = a['href'].replace('/', '#')
        a['href'] = a['href'].upper()

    write_out = open(os.path.join(
        "html_files", "scp-series-contents.html"), 'w', encoding="utf8")
    write_out.write(series1_contents.prettify())

    write_out = open(os.path.join(
        "html_files", "scp-series2-contents.html"), 'w', encoding="utf8")
    write_out.write(series2_contents.prettify())


def remove_crap():

    files = glob.glob(os.path.join(os.getcwd(), "html_files", "*.htm"))
    for file in files:
        soup = BeautifulSoup(open(file, encoding="utf8"))

        # Decompose removes a tag, and everything inside it.
        soup.find("div", id="print-options").decompose()
        soup.find("div", id="print-head").decompose()
        soup.find("div", id="license-area").decompose()
        soup.find("div", id="page-info").decompose()
        soup.find("div", id="dummy-ondomready-block").decompose()
        # Some articles don't have ratings
        if soup.find("span", class_="rateup") is not None:

            soup.find("span", class_="rateup").decompose()
            soup.find("span", class_="ratedown").decompose()
            soup.find("span", class_="cancel").decompose()
            # There's some weird character popping up next to the rating.
            # We have to extract the text from the span tag, then
            # replace the whole span tag with the text.
        if soup.find("span", class_="number prw54353") is not None:
            soup.find("span", class_="number prw54353").unwrap()

        # Some pages have collapsing text. Let's remove the fancy stuff.
        div_cbf = soup.find_all("div", class_="collapsible-block-folded")
        for cbf in div_cbf:
            cbf.find("a").unwrap()

        div_cbuf = soup.find_all("div", class_="collapsible-block-unfolded")
        for cbuf in div_cbuf:
            del cbuf['style']
            cbuf.find(
                "div", class_="collapsible-block-unfolded-link").decompose()

        write_out = open(file, 'w', encoding="utf8")
        write_out.write(str(soup))

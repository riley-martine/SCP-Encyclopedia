"""Turn files into nice html."""

import os
import glob
from bs4 import BeautifulSoup


def create_full_html():
    """Turn all files into html."""
    # It's a text file so that it doesn't get picked up by glob
    result_soup = BeautifulSoup(open(os.path.join("modded_files", 'base.txt'), encoding="utf8"), 'html.parser')

    files = glob.glob(os.path.join(
        os.path.join(os.getcwd(), "html_files", "*.htm")))

    series1_contents = BeautifulSoup(
        open(os.path.join(
            "html_files", "scp-series-contents.html"), encoding="utf8"), 'html.parser')

    result_soup.find("div", id="toc").append(
        series1_contents.find("div", id="main-content"))

    result_soup.find("div", id="toc").append(result_soup.new_tag("br"))

    series2_contents = BeautifulSoup(
        open(os.path.join(
            "html_files", "scp-series2-contents.html"), encoding="utf8"), 'html.parser')

    result_soup.find("div", id="toc").append(
        series2_contents.find("div", id="main-content"))

    result_soup.find("div", id="toc").append(result_soup.new_tag("br"))

    for file in files:
        print("Adding " + file)
        file_soup = BeautifulSoup(open(file, encoding="utf8"), 'html.parser')

        result_soup.find("div", id="articles").append(
            file_soup.find("div", id="container"))
        result_soup.find("div", id="articles").append(
            result_soup.new_tag("br"))

    f = open(os.path.join("encyclopedia", "SCP Encyclopedia.htm"),
             'w', encoding="utf8")
    f.write(result_soup.prettify())
    print("Created Encyclopedia. Location: encyclopedia/SCP Encyclopedia.htm")

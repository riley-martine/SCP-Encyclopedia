"""Download SCPs and Images."""

import urllib.error
import urllib.request
from html.parser import HTMLParser
import os
import shutil
import logging

base_url = 'http://www.scp-wiki.net/printer--friendly/scp-'  # //
starting_scp = 0

# The extra 1 to satisfy our loop
amount_to_get = 2999 + 1  # 2999 default


class ImgParser(HTMLParser):
    """Get images to download."""

    def __init__(self, *args, **kwargs):
        """Reset downlads and init parser."""
        self.downloads = []
        HTMLParser.__init__(self, *args, **kwargs)

    def handle_starttag(self, tag, attrs):
        """Add images to downlads."""
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.downloads.append(attr[1])


def download_files():
    """Actaully download the files."""
    if not os.path.exists("html_files"):
        os.makedirs("html_files")
    if not os.path.exists("encyclopedia"):
        os.makedirs("encyclopedia")

    print("Downloading CSS")
    try:
        urllib.request.urlretrieve(
            "http://static.wikidot.com/v--16f88041ce8d/common--\
theme/base/css/style.css", os.path.join("encyclopedia", "style.css"))

        urllib.request.urlretrieve(
            "http://d3g0gp89917ko0.cloudfront.net/v--16f88041ce8d/common--\
theme/base/css/print.css", os.path.join("encyclopedia", "print.css"))

        urllib.request.urlretrieve(
            "http://d3g0gp89917ko0.cloudfront.net/v--16f88041ce8d/common--\
theme/base/css/print2.css", os.path.join("encyclopedia", "print2.css"))

    # This happens if you have DNS issues, like me. :(
    except urllib.error.URLError as e:
        print(e)
        print("CSS Files" + " couldn't be resolved")
        logging.warning(e)
        logging.warning("CSS Files" + " couldn't be resolved")
        pass


   # except urllib.error.HTTPError:
   #     print("CSS Files" + " couldn't be found")
   #     logging.warning("CSS Files" + " couldn't be found")
   #     pass
    
    # A few files come pre-modified, lets copy them to the necessary dirs.
    shutil.copy(os.path.join("modded_files", "style2.css"), "encyclopedia")
    shutil.copy(os.path.join("modded_files",
                             "scp-series-contents.html"), "html_files")
    shutil.copy(os.path.join("modded_files",
                             "scp-series2-contents.html"), "html_files")

    for current_scp in range(starting_scp, amount_to_get):
        print("-------------")
        print("Starting: " + str(current_scp))

        imgp = ImgParser()
        # This line makes sure that the number has the necessary
        # leading zeros to cooperate with the url.
        # E.g. 2 => 002, and 14 => 014.
        current_url = base_url + ("%03d" % current_scp)

        print("Downloading: " + current_url)

        try:
            urllib.request.urlretrieve(current_url, os.path.join(
                "html_files", os.path.basename(current_url)) + ".htm")

            # Give the page info to ImgHandler so it can find add the images it
            # needs to download

            imgp.feed(open(os.path.join("html_files", os.path.basename(
                current_url)) + ".htm", encoding="utf8").read())

            # Download all the urls created by ImgHandler
            for path in imgp.downloads:

                if(not path.startswith('http')): # No :// allows detection of https
                    path = "http://scp-wiki.wdfiles.com" + path
                if(path.find('?') is not -1):
                    path = path.split('?')[0]
                if(path.find('"') is not -1):
                    path = path.replace('"', '')

                print("Getting image: " + path)
                urllib.request.urlretrieve(path, os.path.join(
                    "encyclopedia", os.path.basename(path)))

        # This happens if you have DNS issues, like me. :(
        except urllib.error.URLError:
            print(current_url + " cannot be resolved")
            logging.warning(current_url + " cannot be resolved")
            pass


        except urllib.error.HTTPError:
            print(current_url + " not found")
            logging.warning(current_url + " not found")
            pass
        


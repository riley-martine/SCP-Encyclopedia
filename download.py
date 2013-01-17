import urllib.error
import urllib.request
from html.parser import HTMLParser
import os
import shutil

base_url = 'http://www.scp-wiki.net/printer--friendly//scp-'
current_scp = 0

# The extra 1 to satisfy our loop
amount_to_get = 1999 + 1

class ImgParser(HTMLParser):
        def __init__(self, *args, **kwargs):
            self.downloads = []
            HTMLParser.__init__(self, *args, **kwargs)
        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                for attr in attrs:
                    if attr[0] == 'src':
                        self.downloads.append(attr[1])
                

def download_files():

    if not os.path.exists("html_files"):
            os.makedirs("html_files")
    if not os.path.exists("encyclopedia"):
            os.makedirs("encyclopedia")
        
    print("Downloading CSS")
    urllib.request.urlretrieve("http://static.wikidot.com/v--16f88041ce8d/common--theme/base/css/style.css", os.path.join("encyclopedia", "style.css"))
    urllib.request.urlretrieve("http://d3g0gp89917ko0.cloudfront.net/v--16f88041ce8d/common--theme/base/css/print.css", os.path.join("encyclopedia", "print.css"))
    urllib.request.urlretrieve("http://d3g0gp89917ko0.cloudfront.net/v--16f88041ce8d/common--theme/base/css/print2.css", os.path.join("encyclopedia", "print2.css"))

    # A few files come pre-modified, lets copy them to the necessary dirs.
    shutil.copy(os.path.join("modded_files", "style2.css"), "encyclopedia")
    shutil.copy(os.path.join("modded_files", "scp-series-contents.html"), "html_files")
    shutil.copy(os.path.join("modded_files", "scp-series2-contents.html"), "html_files")
                    
    for current_scp in range(1, amount_to_get):
        print("-------------")
        print("Starting: " + str(current_scp))

        imgp = ImgParser()
        # This line makes sure that the number has the necessary
        # leading zeros to cooperate with the url.
        # E.g. 2 => 002, and 14 => 014.
        current_url = base_url + ("%03d" % current_scp)

        print("Downloading: " + current_url)
        page = urllib.request.urlretrieve(current_url, os.path.join("html_files", os.path.basename(current_url)) + ".htm")

        # Give the page info to ImgHandler, so it can find add the images it
        # needs to download

        imgp.feed(open(os.path.join("html_files", os.path.basename(current_url)) + ".htm", encoding="utf8").read())

        # Download all the urls created by ImgHandler
        for path in imgp.downloads:
                if(path.startswith('/local--files')):
                        path = "http://scp-wiki.wdfiles.com" + path
                        print("Path was relative to local--files")
                print("Getting image: " + path)
                urllib.request.urlretrieve(path, os.path.join("encyclopedia", os.path.basename(path)))


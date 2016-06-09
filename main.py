"""Download and process files."""

import sys
import createhtml
import download
import processing

print(sys.executable)

download.download_files()
processing.abs_paths_to_rel()
processing.remove_crap()
createhtml.create_full_html()

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/88233032ccae4bb8b7244446e0d8da6b)](https://www.codacy.com/app/***REMOVED***/SCP-Encyclopedia?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=riley-martine/SCP-Encyclopedia&amp;utm_campaign=Badge_Grade)
SCP-Encyclopedia
================
I forked this from the original author, Matthood, whose readme is below. I have so far not added any new features, only fixed existing ones. Namely: gitignore for downloaded files, don't fail on 404, image links to images folder rather than to html_files folder.


Hey everyone.
As the description says, this script will download the Series 1 - 3 SCP articles. It downloads images, and even throws in a table of contents with # style anchors to the articles.

The only dependecy is Python 3. I've included Beautiful Soup (thanks heaps Datastream), so no need to go downloading libraries. Also, if you want to start again, make sure to delete the 'encyclopedia' & 'html_files' directories.

The script, as I said, only generates a html file (in 'encyclopdia'). Pop it into your favorite PDF authoring tool. As long as it supports anchors, you're all gravy.


To make stuff happen:

python3 main.py


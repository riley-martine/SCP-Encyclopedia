[![Codacy Badge](https://api.codacy.com/project/badge/Grade/88233032ccae4bb8b7244446e0d8da6b)](https://www.codacy.com/app/***REMOVED***/SCP-Encyclopedia?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=riley-martine/SCP-Encyclopedia&amp;utm_campaign=Badge_Grade)
SCP-Encyclopedia
================

Hey everyone.
As the description says, this script will download the Series 1 - 3 SCP articles. It downloads images, and even throws in a table of contents with # style anchors to the articles. Full size of everything (downloaded once and compiled once) is ~500M.


The script  generates an html file (in 'encyclopdia'). Pop it into your favorite PDF authoring tool or browser. As long as it supports anchors, you're all gravy.


To make stuff happen:

-pip3 install -r requirements.txt

-python3 main.py

-check the error.log

-Generated file is encyclopedia/SCP Encyclopedia.htm

# TODO

Todo List
- Retry instead of failing on socket.gaierror
- Add output options:
- - onefile: all in one file, images inlined
- - nametbd: directory including file, img directory, css directory
- - manyfile: many files, one for each SCP. Ideal: have "next" link.
- Handle SCP-001
- Test Other SCPs for completeness
- Option for less bare pages
- See what happens if two images have the same name
- Don't redownload files unless asked to
- Make into python package?

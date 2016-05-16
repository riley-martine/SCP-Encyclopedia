SCP-Encyclopedia
================
I take no credit for this, only updating bs so it would run. I will attempt to improve it in the future. Below is the original author's readme. 


Hey everyone. 
As the description says, this script will download the Series 1 & 2 SCP articles, 
and concatenate (love that word) them into a single html file. It downloads images, 
and even throws in a table of contents with # style anchors to the articles.

The only dependecy is Python 3. I've included Beautiful Soup (thanks heaps Datastream),
so no need to go downloading libraries. Also, if you want to start again, make sure to delete 
the 'encyclopedia' & 'html_files' directories.

The script, as I said, only generates a html file (in 'encyclopdia'). Pop it into your favorite PDF 
authoring tool. As long as it supports anchors, you're all gravy.

Finally, this is very Beta. Likely to fall over with little to no notice. Due to internet bandwith
constraints, I've only tested it with the first 10 SCP's! If you can read this, expect it to screw 
up on SCP-011! Please submit an issue to Github when it does.
 
To make stuff happen:
--
python main.py
--



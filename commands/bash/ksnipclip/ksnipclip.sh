#!/usr/bin/bash

ksnip --rectarea --saveto /tmp/screenshot.png
xclip -sel clip -t image/png -in /tmp/screenshot.png
rm /tmp/screenshot.png

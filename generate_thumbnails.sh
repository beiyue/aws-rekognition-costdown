#!/bin/bash

sudo ffmpeg -i $1 -an -vf select='eq(pict_type\,I)' -vsync 2 -s 720*480  -f image2  $2/image-%03d.jpg

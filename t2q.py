# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re
import sys
from PIL import Image

#########################
black = '0'  # Can't be #
blank = '1'  # SPACES   #
#########################

if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 2:
        print("Usage: python t2q.py <file.txt>")
        sys.exit(0)
    if not os.path.isfile(sys.argv[1]) or not sys.argv[1].endswith('.txt'):
        print("Invalid file")
        sys.exit(1)
    with open(sys.argv[1].replace('\\', '/')) as raw_f:
        for raw_contain in raw_f:
            if not re.search('[^' + black + blank + '\\n]', raw_contain) is None:
                print("Invalid content")
                print("The contents of the file can only contain " + black + " and " + blank + " and \\n")
                sys.exit(1)
#
        raw_f.seek(0)
        qr_x = len(raw_f.readline()) - 1
        raw_f.seek(0)
        qr_y = len(raw_f.readlines())
        raw_f.seek(0)
        pic = Image.new('RGB', (qr_x, qr_y))
        y = 0
        for raw_contain_deal in raw_f:
            i = 0
            for x in range(0, qr_x):
                if raw_contain_deal[i] == black:
                    pic.putpixel([x, y], (0, 0, 0))
                else:
                    pic.putpixel([x, y], (255, 255, 255))
                i += 1
            y += 1
    pic.show()
    pic.save('output.png')


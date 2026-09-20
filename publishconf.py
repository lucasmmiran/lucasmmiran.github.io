#!/usr/bin/env python
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pelicanconf import *

# Troque pela URL real do GitHub Pages, ex:
# https://<usuario>.github.io  ou  https://<usuario>.github.io/<repo>
SITEURL = 'https://lucasmmiranda.github.io'

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

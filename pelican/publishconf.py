#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://erenturkay.com/blog'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
READ_MORE_LINK_FORMAT = '<a class="read-more" href="%s/{url}">{text}</a>' % SITEURL

# Following items are often useful when publishing

TAGLINE = """System administrator, software developer, linux enthusiast,
and hamradio operator. Work @SkyAtlas"""

DISQUS_SITENAME = 'erenturkay-blog'
USER_LOGO_URL = "http://erenturkay.com/images/avatar.jpeg"

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

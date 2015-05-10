#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGINS = ['plugins.read_more_link', 'plugins.sitemap']

AUTHOR = u'Eren T\xfcrkay'
SITENAME = u'Eren T\xfcrkay | Blog'
SITEURL = 'http://localhost:8000'

SITEMAP = {
    'format': 'xml'
}

PATH = 'content'
OUTPUT_PATH = '../blog/'

TIMEZONE = 'Europe/Istanbul'

THEME = "theme/pelican-svbhack"

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

SUMMARY_MAX_LENGTH = 75
READ_MORE_LINK = '<span>continue reading</span>'
READ_MORE_LINK_FORMAT = '<a class="read-more" href="%s/{url}">{text}</a>' % SITEURL

# Social widget
SOCIAL = (
            ('About', 'http://erenturkay.com/'),
            ('Github', 'https://github.com/eren/'),
            ('Twitter', 'https://twitter.com/erenturkay'),
         )

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Robert Kyle'
SITENAME = u'Image Awesome Blog'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', '//twitter.com/robtheforager'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PLUGIN_PATHS = ['plugins']
#PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.include_code', 'liquid_tags.notebook']
PLUGINS = ['liquid_tags.notebook']

EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

import os
THEME = os.path.join(os.getcwd(), 'imageawesome_theme')

SITEURL = 'http://' + os.environ.get('BLOGHOST', 'blog.imageawesome.com')
WEBURL = '//' + os.environ.get('WEBHOST', 'imageawesome.com')

DISQUS_SITENAME = 'imageawesome'

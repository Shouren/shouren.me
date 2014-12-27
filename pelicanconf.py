#!/usr/bin/env python3.3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'shouren'
SITENAME = "Shouren's blog"
SITEURL = 'http://shouren.me'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/rss.xml'
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Pelican Theme
THEME = '/Users/kimi/Documents/Dev/blog/shouren.me/themes/pelican-bootstrap3'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('CT', 'http://chentingpc.me'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/kimi_ysr'),
        ('GitHub', 'https://github.com/Shouren'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = (['codehilite(css_class=highlight)', 'extra'])

PLUGIN_PATHS = ['/Users/kimi/Documents/Dev/blog/shouren.me/plugins']
PLUGINS = ['summary', 'gravatar', 'extract_toc', 'latex', 'sitemap']

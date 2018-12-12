# !/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'shouren'
SITENAME = "Shouren's blog"
SITEURL = 'https://blog.shouren.me'

PATH = './content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Pelican Theme
THEME = './theme/pelican-blue'

# Blogroll
LINKS = (
            ('RSS', SITEURL + '/' + FEED_ALL_ATOM),
            ('Pelican', 'http://getpelican.com/'),
            ('Python.org', 'http://python.org/'),
            ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (
            ('Twitter', 'https://twitter.com/_shouren'),
            ('GitHub', 'https://github.com/Shouren'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['summary', 'gravatar', 'extract_toc', 'latex', 'sitemap']

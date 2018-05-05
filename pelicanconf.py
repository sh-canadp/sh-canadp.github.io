#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ShizaCat'
SITENAME = 'Sh.Can.Adp'
SITEURL = 'sh-canadp.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub', 'http://github.com/'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites',]

# THEME = 'localized_theme'

STATIC_PATHS = ['images', 'files']

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
	'ru': {
	    # 'SITENAME': 'Уж и  не знаю как назвать',
	    'STATIC_PATHS': ['images', 'files'],
		'MENUITEMS': (
			('Статьи', '/archives'),
		),
		'THEME': './nest',
		'NEST_ARCHIVES_HEADER_TITLE': 'Статьи',
		'NEST_ARCHIVES_CONTENT_TITLE': 'Материалы, новости',
	},
	'en': {
		# 'SITENAME': 'English -- timtle site',
		'STATIC_PATHS': ['images', 'files'],
		'MENUITEMS': (
			('Articles', '/archives'),
		),
		'THEME': './nest',
		'NEST_ARCHIVES_HEADER_TITLE': 'Articles',
		'NEST_ARCHIVES_CONTENT_TITLE': 'Materials & news',
	}
}

# --- Thema
THEME = './nest'

NEST_HEADER_LOGO = '/images/logo.png'
# NEST_ARCHIVES_HEADER_SUBTITLE = ''

# --- Settings from localization
MENUITEMS = I18N_SUBSITES['ru']['MENUITEMS']

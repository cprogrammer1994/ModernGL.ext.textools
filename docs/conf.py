#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.githubpages', 'sphinx.ext.intersphinx', 'sphinxcontrib.napoleon']

templates_path = ['templates']
source_suffix = '.rst'

master_doc = 'index'

project = 'ModernGL.ext.textools'
copyright = '2017, Szabolcs Dombi'
author = 'Szabolcs Dombi'

version = '0.2.0'
release = '0.2.0'

language = None

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['static']

htmlhelp_basename = 'ModernGL.ext.textools.doc'

latex_elements = {}

latex_documents = [
    (master_doc, 'ModernGL.ext.textools.tex', 'ModernGL.ext.textools Documentation', 'Szabolcs Dombi', 'manual'),
]

man_pages = [
    (master_doc, 'ModernGL.ext.textools', 'ModernGL.ext.textools Documentation', [author], 1)
]

texinfo_documents = [
    (
        master_doc,
        'ModernGL.ext.textools',
        'ModernGL.ext.textools Documentation',
        author,
        'ModernGL.ext.textools',
        'One line description of project.',
        'Miscellaneous'
    ),
]

intersphinx_mapping = {
    'ModernGL': ('https://moderngl.readthedocs.io/en/stable/', None),
    'Pillow': ('https://pillow.readthedocs.io/en/stable/', None),
}


def setup(app):
    app.add_stylesheet('css/custom.css')


autodoc_member_order = 'bysource'
# autodoc_member_order = 'groupwise'
add_module_names = False

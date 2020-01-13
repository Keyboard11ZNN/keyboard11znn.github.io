# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
sys.path.insert(0, os.path.abspath('./_ext'))

# -- Project information -----------------------------------------------------

project = 'Keyboard11 z n. n. website'
copyright = '2020+, stan423321'
author = 'stan423321'

# The full version, including alpha/beta/rc tags
release = 'tbd'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'k11specials'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# we all know the only language at which I'm not completely incompetent is C++
# so this will probably shorten stuff -- stan
primary_domain = 'cpp'
highlight_language = 'cpp'


# -- Options for HTML output -------------------------------------------------

html_theme = 'classic'
html_theme_options = {
    'collapsiblesidebar': True,
    'externalrefs': True,
}
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# here's my super turbo fancy minimal logo which totally didn't take forever
# to make - stan
html_logo = '_static/keyboard11banner.svg'
html_favicon = '_static/favicon.ico'
# the default title is kind of redundant though
html_title = 'KEYBOARD11 z n. n.'
# this is kinda unlikely, but still
htmlhelp_basename = 'kbrd11'



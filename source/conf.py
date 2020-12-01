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

# -- Project information -----------------------------------------------------

project = 'IQM Spring 2020'
copyright = '2020, Vincent Meunier'
author = 'Vincent Meunier'


# -- General configuration ---------------------------------------------------


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
#import edx_theme
#import os

#extensions = []
#html_theme = 'edx_theme'
#html_theme_path = [edx_theme.get_html_theme_path()]
#html_favicon = os.path.join(html_theme_path[0], 'edx_theme', 'static', 'css', 'favicon.ico')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.imgmath',
#    'sphinxcontrib.yt',
#    'sphinx.ext.todo',
#    'sphinx.ext.githubpages',
#    'edx_theme'
]

latex_elements = {
    'preamble': r'''
\usepackage{physics}
''',
'extraclassoptions': 'openany,oneside'
}

latex_show_urls = 'footnote'

imgmath_add_tooltips = True
imgmath_latex_preamble=r'\usepackage{physics}'
imgmath_image_format='svg'

master_doc = 'index'

latex_documents = [
    (master_doc, 'edx-sphinx-theme.tex', 'Introduction to Quantum Mechanics',
     author, 'manual'),
]

#import edx_theme
#import os

#extensions = ['edx_theme']

#html_theme = 'edx_theme'
#html_theme_path = [edx_theme.get_html_theme_path()]
#html_favicon = os.path.join(html_theme_path[0], 'edx_theme', 'static', 'css', 'favicon.ico')

html_logo =  '_images/iqm_logo.png'
logo_only = True
display_version = True
numfig = False

from pallets_sphinx_themes import ProjectLink, get_version

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Raster Vision'
copyright = '2018, Azavea'
author = 'Azavea'

# The short X.Y version
version = '0.13'
# The full version, including alpha/beta/rc tags
release = '0.13.0'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'pallets_sphinx_themes',
    'sphinx.ext.napoleon',
]

# https://read-the-docs.readthedocs.io/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
import sys
from unittest.mock import MagicMock


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = ['pyproj', 'h5py', 'osgeo', 'mask_to_polygons']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

autodoc_mock_imports = ['torch', 'torchvision', 'pycocotools']

intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# HTML -----------------------------------------------------------------

html_theme = 'click'
html_theme_options = {'index_sidebar_logo': False}
html_context = {
    'project_links': [
        ProjectLink('Quickstart', 'quickstart.html'),
        ProjectLink('Documentation TOC', 'index.html#documentation'),
        ProjectLink('Examples', 'examples.html'),
        ProjectLink('Config API Reference', 'index.html#api'),
        ProjectLink('AWS Batch Setup', 'cloudformation.html'),
        ProjectLink('Project Website', 'https://rastervision.io/'),
        ProjectLink('PyPI releases', 'https://pypi.org/project/rastervision/'),
        ProjectLink('GitHub Repo', 'https://github.com/azavea/raster-vision'),
        ProjectLink('Gitter Channel',
                    'https://gitter.im/azavea/raster-vision'),
        ProjectLink('Issue Tracker',
                    'https://github.com/azavea/raster-vision/issues/'),
        ProjectLink('CHANGELOG', 'changelog.html'),
        ProjectLink('Azavea', 'https://www.azavea.com/'),
    ],
    'css_files': [
        '_static/rastervision.css',
        'https://media.readthedocs.org/css/badge_only.css'
    ]
}
html_sidebars = {
    'index': ['project.html', 'versions.html', 'searchbox.html'],
    '**': [
        'project.html', 'localtoc.html', 'relations.html', 'versions.html',
        'searchbox.html'
    ],
}
singlehtml_sidebars = {
    'index': ['project.html', 'versions.html', 'localtoc.html']
}
html_static_path = ['_static']
html_favicon = 'img/raster-vision-icon.png'
html_logo = 'img/raster-vision-logo.png'
html_title = 'Raster Vision Documentation ({})'.format(version)
html_show_sourcelink = False
html_domain_indices = False
html_experimental_html5_writer = True

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'RasterVisiondoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'RasterVision.tex', 'Raster Vision Documentation', 'Azavea',
     'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'RasterVisoin-{}.tex', html_title, [author],
              'manual')]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'RasterVision', 'Raster Vision Documentation', author,
     'RasterVision', 'One line description of project.', 'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

programoutput_prompt_template = '> {command}\n{output}'

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

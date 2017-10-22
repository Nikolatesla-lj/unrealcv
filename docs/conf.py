#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, glob, shutil, subprocess, hashlib, json
doc_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(doc_dir)
sys.path.insert(0, doc_dir)

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    # If runs on ReadTheDocs environment
    print('Fetching files with git_lfs for %s' % project_dir)
    # Hack for lacking git-lfs support ReadTheDocs
    import git_lfs
    git_lfs.fetch(project_dir)

    # Generate xml from doxygen
    subprocess.call(['doxygen', 'Doxyfile'])

import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx_issues',
    'nbsphinx',
    'sphinx.ext.napoleon',
    # support doc string with section titles
    'sphinx.ext.autosummary',
]

# Github repo
issues_github_path = 'unrealcv/unrealcv'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
} # Markdown support

source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
# master_doc = 'index'
master_doc = 'contents'
# master_doc = 'README'

# General information about the project.
project = 'UnrealCV'
copyright = '2017, UnrealCV team'
author = 'UnrealCV contributors'

def parse_unrealcv_version(unrealcv_folder):
    plugin_descriptor = os.path.join(unrealcv_folder, 'UnrealCV.uplugin')
    with open(plugin_descriptor) as f:
        description = json.load(f)
    plugin_version = description['VersionName']
    return plugin_version

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = parse_unrealcv_version('..')
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# Folder can not end with /
exclude_patterns = [
    '_build/',
    '**/Thumbs.db',
    '**/.DS_Store/',
    '**/.ipynb_checkpoints'
]

print(exclude_patterns)

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
# todo_include_todos = False
todo_include_todos = True


html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'logo_only': False,
}


# Output file base name for HTML help builder.
htmlhelp_basename = 'UnrealCVDoc'

# extensions.append('breathe') # Support doxygen
# breathe_projects = {
#     "unrealcv": "./doxygen/xml/",
# }
# breathe_default_project = 'unrealcv'

# Some extra configurations of sphinx
# Reference: http://www.sphinx-doc.org/en/stable/config.html
numfig = True

suppress_warnings = ['image.nonlocal_uri']
# Some images are hosted outside this project to reduce the repo size, so I don't care about this warning.

nitpicky = True
nitpick_ignore = [('py:obj', 'str'), ('py:obj', 'bool')]

# Fix lexer issue for anaconda ipython
# from https://github.com/tomoh1r/symfony-docs-trans-env/issues/6
# and https://github.com/ContinuumIO/anaconda-issues/issues/1430
from sphinx.highlighting import lexers
from pygments.lexers.python import PythonLexer
lexers['ipython2'] = PythonLexer()
lexers['ipython3'] = PythonLexer()

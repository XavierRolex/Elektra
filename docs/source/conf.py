# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# The general information about your project (project name, author, etc.)

project = 'Elektra'
copyright = '2025, Israt Zaman Srity'
author = 'Israt Zaman Srity'
release = '1.0'

# -- General configuration ---------------------------------------------------
# General settings for Sphinx, including extensions and paths.

extensions = [
    'sphinx.ext.autodoc',  # Automatically document your code (models, views, etc.)
]

# Paths to your templates
templates_path = ['_templates']

# Exclude patterns for files/folders you don't want in your documentation
exclude_patterns = []

# -- Path setup -----------------------------------------------------
# Add your Django project to the sys.path so Sphinx can find it

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Path to your Django project
os.environ['DJANGO_SETTINGS_MODULE'] = 'Elektra.settings'  # Your Django settings file
import django
django.setup()  # Initialize Django

# -- Options for HTML output -------------------------------------------------
# Configuration for the HTML output of the documentation

html_theme = 'alabaster'  # Default theme for the documentation
html_static_path = ['_static']  # Path for custom static files like CSS or images


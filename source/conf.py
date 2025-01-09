# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SCANOSS Settings'
copyright = '2024, Scan Open Source Solutions SL'
author = 'Scan Open Source Solutions SL'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_logo = 'SCANOSSDocsLogo.jpg'
html_static_path = ['_static']

html_theme_options = {
     'body_max_width': 'none',
     #'sidebarwidth': '10%',  # Make sidebar relative
     #'documentwidth': '80%'  # Make main content relative
}
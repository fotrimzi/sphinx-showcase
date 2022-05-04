# -*- coding: utf-8 -*-
import os, sys, sphinx
import acdocutils

project = 'Sphinx Test Documents'
version = '1.0'
sphinx_version = sphinx.__version__
rel = acdocutils.get_release_version(version)
release = "%s (Sphinx %s)" % (rel, sphinx_version)
release = rel
# Chapter number prefix text. Default is ''. Uncomment this to override.
chapter_text = 'Section'

title = 'Sphinx Showcase'

latex_documents = [
    ('index', 'ac-doc-test-%s.tex' % rel,      title, 'Test Document', 'ac-guide'),
  # ('test/index', 'ac-doc-test-plain.tex', latex_title, 'Test Coverage Document (Plain)', 'manual')
]

# tocdepth = 4 # Override default for PDF TOC level

extensions = [
    # 'ac_ref',
    # 'ac_table', # TODO - remove
    'ac_appendix',
    'acattr',
    'acerr',
    'acfn',
    'acobj',
    'acop',
    'acprg',
    'actyp',
    'acapiattr',
    'acapiobj'
]

project_replacements = {
    'mycustom': 'Test Replacement from properties.py',
    'my_custom_too': 'Another Test Replacement from properties.py',
    'sphinx_version': sphinx.__version__,
    # Used for included install steps:
    'section': 'Applications',
    # (downloaded package name, with extension variations)
    'package': 'ac-doc-%s-pkg' % release,
    'downloaded_package': 'ac-doc-%s-pkg.tar.gz' % release,
    'product': 'Sphinx Showcase'
}

man_pages = [('ac_bl','ac_bl','Batch updates of RDBMS data',['Asset Control'],1)]

publish_to = ['webdoc','TEST/%s %s' % (project, version)]

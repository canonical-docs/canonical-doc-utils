#!/usr/bin/env python3

from setuptools import setup, find_packages
import CanonicalDocUtils

setup(name='CanonicalDocUtils',
      version=CanonicalDocUtils.__version__,
      description='Utilities for managing docs team tasks',
      author='Canonical Docs team',
      author_email='nick.veitch+pypi@canonical.com',
      url='https://www.github.com/evilnick/canonical-doc-utils',
      license="AGPLv3+",
      packages=find_packages(),
      install_requires=[
        "sh>=1.12.0",
        "PyGithub>=1",
        "requests>=2.8.1",
        "PyYAML>=1",
      ],
      entry_points={
        'console_scripts': [
            'docs-backport=CanonicalDocUtils.cli.bporter:main',
            'docs-cleanfork=CanonicalDocUtils.cli.cleanfork:main',
            'docs-juju-commandgen=CanonicalDocUtils.cli.commandgen3:main',
            'docs-discourse-put=CanonicalDocUtils.cli.discourse_put:main',
        ],

    }

     )

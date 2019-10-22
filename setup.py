#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages
import re
import os
import sys
import codecs


name = 'fixmydjango'
package = 'fixmydjango'
description = 'A Django app for finding solutions to exceptions'
url = 'http://github.com/vintasoftware/fixmydjango-lib'
author = 'Flávio Juvenal da Silva Junior'
author_email = 'flavio@vinta.com.br'
license = 'MIT'
install_requires = [
    'Django >= 1.4, < 2',
    'requests == 2.20.0',
    'boltons == 16.1.1',
    'termcolor == 1.1.0',
]


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_long_description():
    with codecs.open('README.rst', 'r', 'utf-8') as f:
        return f.read()


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


# python setup.py register
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    long_description=get_long_description(),
    author=author,
    author_email=author_email,
    packages=find_packages(exclude=['*.tests']),
    package_data=get_package_data(package),
    install_requires=install_requires,
    test_suite='tox'
)

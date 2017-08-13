#
# Copyright 2017 Wenter
#
# https://yowenter.github.io
#

import os
import re

from setuptools import find_packages
from setuptools import setup

with open('__version__.py', "r") as f:
    source = f.read()
    m = re.search("__version__ = '(.*)'", source, re.M)
    __version__ = m.groups()[0]

with open('README.rst', 'r') as readme:
    long_description = readme.read()

setup(
    name="taoge-blog",
    version=__version__,
    description="[Taoge Blog](https://yowenter.github.io)",
    long_description=long_description,
    author="Wenter W",
    author_email="wenter.wu@gmail.com",
    license="MIT License",
    url="https://github.com/yowenter/yowenter.github.io",
    keywords="taoge blog; yowenter; taoge's thoughts; wenter.wu#gmail",
    classifiers=[
        'Programming Language :: Python :: 2.7'
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Sphinx",
        "sphinxcontrib-httpdomain",
        "sphinxcontrib-newsfeed",
        "recommonmark"],
    zip_safe=False,
)

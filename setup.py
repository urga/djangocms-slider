#!/usr/bin/env python
import os
from setuptools import setup


INSTALL_REQUIRES = [
    "django-admin-sortable==1.6.7",
]

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Natural Language :: Dutch",
    "Natural Language :: English",
    "Programming Language :: Python :: 2.7",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Multimedia :: Graphics :: Viewers",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    "Operating System :: OS Independent",
]


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "djangocms-slideshow",
    version = "0.1.0",
    author = "Urga",
    author_email = "dries@urga.be",
    description = "A simple django cms slideshow plugin",
    long_description=read('README.txt'),
    license = "GNU",
    keywords = ["slideshow", "django", "cms", "plugin"],
    url = "",
    packages=['slideshow', ],
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
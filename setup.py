#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

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

setup(
    name = "djangocms-slideshow",
    version = "0.1.3",
    author = "Urga",
    author_email = "dries@urga.be",
    description = "A simple django cms slideshow plugin",
    license = "GNU",
    keywords = ["slideshow", "django", "cms", "plugin"],
    url = "https://github.com/urga/djangocms-slideshow",
    packages=['slideshow', 'slideshow.migrations', ],
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    long_description=read('README.md'),
    include_package_data=True,
    zip_safe=False
)
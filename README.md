djangocms-slideshow
===================

A simple django cms slideshow plugin.

Features:

* The images can be arranged.
* Each image can have a url specified (creating an anchor around the image)

Installation
------------

This plugin requires `django CMS 3.0` or higher to be properly installed and configured.

To install:

* run `pip install djangocms-slideshow` on your virtualenv
* add `slideshow` to your `INSTALLED_APPS` setting
* Run `./manage.py migrate slideshow`
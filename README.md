djangocms-slideshow
===================

A simple django cms slideshow plugin.

Features:

* The images can be arranged.
* Each image can have a url specified (creating an anchor around the image)
* By default, creates a [flexslider](http://www.woothemes.com/flexslider/) slideshow.

Installation
------------

This plugin requires `django CMS 3.0` or higher to be properly installed and configured.

To install:

* run `pip install djangocms-slideshow` on your virtualenv
* add `slideshow` to your `INSTALLED_APPS` setting
* Run `./manage.py migrate slideshow`

Usage
-----

To use a custom template, just add `slideshow.html` in directory `templates/slideshow` of your Django project.
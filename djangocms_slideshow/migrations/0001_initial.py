# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='cms.CMSPlugin', serialize=False)),
                ('image', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='image')),
                ('url', models.CharField(blank=True, null=True, help_text='If present, clicking on image will take user to link.', verbose_name='link', max_length=255)),
                ('caption', models.TextField(blank=True, null=True, help_text='Specifies text that occurs on the slide.', verbose_name='caption', max_length=255)),
                ('page_link', models.ForeignKey(verbose_name='page', blank=True, null=True, to='cms.Page', help_text='If present, clicking on image will take user to specified page.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='cms.CMSPlugin', serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

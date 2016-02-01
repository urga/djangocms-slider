# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='image')),
                ('url', models.CharField(help_text='If present, clicking on image will take user to link.', max_length=255, null=True, verbose_name='link', blank=True)),
                ('caption', models.TextField(help_text='Specifies text that occurs on the slide.', max_length=255, null=True, verbose_name='caption', blank=True)),
                ('page_link', models.ForeignKey(blank=True, to='cms.Page', help_text='If present, clicking on image will take user to specified page.', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

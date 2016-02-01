from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from djangocms_slider.cms_plugins import SliderPlugin


class SliderPluginTests(TestCase):
    def setUp(self):
        self.plugin_class = SliderPlugin
        self.placeholder = Placeholder.objects.create(slot='test')

    def test_sliderplugin_context(self):
        """
        test wether the plugin/model instance is in the context
        """
        model_instance = add_plugin(self.placeholder, self.plugin_class, language='en')
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('instance', context)

    def test_sliderplugin_template(self):
        model_instance = add_plugin(self.placeholder, self.plugin_class, language='en')
        html = model_instance.render_plugin()
        self.assertTrue(html.find('<div class="slider">') > -1)

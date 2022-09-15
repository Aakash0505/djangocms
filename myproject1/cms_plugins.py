from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext as _
from .models import Poem


@plugin_pool.register_plugin  # register the plugin
class PoetryPlugin(CMSPluginBase):
    model = Poem  # model where plugin data are saved
    render_template = "mypoems.html"
    cache = False

   
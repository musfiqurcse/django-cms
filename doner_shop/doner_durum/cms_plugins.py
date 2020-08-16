from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import *

class Daily_Special_Plugin(CMSPluginBase):
    model=Daily_Specials
    name = "Daily Specials Filer"
    render_template = "daily_special.html"


    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,
            'url': instance.url

        })
        return context




plugin_pool.register_plugin(Daily_Special_Plugin)
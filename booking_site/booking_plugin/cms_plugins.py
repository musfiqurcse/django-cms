from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *

@plugin_pool.register_plugin
class Daily_Offers_Plugin(CMSPluginBase):
    model = Daily_Offers
    name = "Daily Offers"
    render_template = "daily_offers.html"


    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,
            'url': instance.url
        })
        return context






@plugin_pool.register_plugin
class Offers_plugin(CMSPluginBase):
    model = Offers
    name = "Offers"
    render_template = "offers.html"


    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,
            'url': instance.url,
            'price': instance.price
        })
        return context
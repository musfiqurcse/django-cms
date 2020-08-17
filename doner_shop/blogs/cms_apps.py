from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class BlogApp(CMSApp):
    name = "Blogs"
    urls = ["blogs.urls"]
    app_name = "blogs"

# apphook_pool.register(BlogApp)
    def get_urls(self, page=None, language=None, **kwargs):
        return ['blogs.urls']

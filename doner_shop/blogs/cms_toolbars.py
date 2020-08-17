from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break, SubMenu

@toolbar_pool.register
class PostToolBar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu("blog-menu", "Blogs")
        position = admin_menu.get_alphabetical_insert_position("Posts", SubMenu)
        post_menu = admin_menu.get_or_create_menu("post-menu", "Posts", position=position)


        url="/admin/blogs/posts"

        post_menu.add_modal_item("Edit Posts", url=url)
        url="/admin/blogs/posts/add"
        post_menu.add_modal_item("Add new Post", url=url)
        post_menu.add_break()



@toolbar_pool.register
class CategoryToolBar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu("blog-menu", "Blogs")
        position = admin_menu.get_alphabetical_insert_position("Category", SubMenu)
        category_menu = admin_menu.get_or_create_menu("category-menu", "Category", position=position)


        url="/admin/blogs/category"

        category_menu.add_modal_item("Edit Category", url=url)
        url="/admin/blogs/category/add"
        category_menu.add_modal_item("Add new Category", url=url)
        category_menu.add_break()
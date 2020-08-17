from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog_item'),
    path('category/<int:c_id>', views.category, name='category_item'),
    path('post/<int:p_id>',  views.post, name='post_item'),
]

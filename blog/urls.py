from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /
    url(r'^$', views.post_list, name='post_list'),
    # ex: /post/1/
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # ex: /post/new/
    url(r'^post/new/$', views.post_new, name='post_new'),
    # ex: /post/1/edit/
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

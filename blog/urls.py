from django.urls import path, re_path
from . import views

urlpatterns = [
    # ex: /
    path('', views.post_list, name='post_list'),
    # ex: /post/1/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # ex: /post/new/
    path('post/new/', views.post_new, name='post_new'),
    # ex: /post/1/edit/
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # ex: /drafts/
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # ex: /post/1/publish/
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    # ex: /post/1/remove/
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    # ex: /post/1/comment/
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # ex: /comment/1/approve/
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    # ex: /comment/1/remove/
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]

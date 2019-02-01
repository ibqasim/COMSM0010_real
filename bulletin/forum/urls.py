from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),
    path('thread/create/', views.create, name='create'),
    path('thread/create_thread/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/', views.thread, name='thread'),
    path('thread/<int:thread_id>/post/', views.post, name='post'),
]



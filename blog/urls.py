from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('read_post/<int:id>', views.read_post, name='read_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<int:id>', views.update_post, name='update_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('edit_comment/<int:id>', views.edit_comment, name='edit_comment'),
]

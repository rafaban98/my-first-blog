from django.urls import path
from .import views
#add a url pattern
urlpatterns = [
    path('', views.post_list,name=' post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
 ]
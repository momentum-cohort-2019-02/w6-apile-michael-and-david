from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('tagged/<slug:slug>/', views.tagged_list, name='tagged_list'),
    path('<slug:slug>/like/', views.like_post, name='like_post')
]

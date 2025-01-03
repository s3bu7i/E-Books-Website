from django.urls import path
from . import views

urlpatterns = [
    path('', views.ebook_list, name='ebook_list'),
    path('ebook/<int:pk>/', views.ebook_detail, name='ebook_detail'),
    path('ebook/new/', views.ebook_create, name='ebook_create'),
    path('ebook/<int:pk>/edit/', views.ebook_update, name='ebook_update'),
    path('ebook/<int:pk>/delete/', views.ebook_delete, name='ebook_delete'),
]

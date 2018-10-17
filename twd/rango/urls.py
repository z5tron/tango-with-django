from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('category/<slug:category_name_slug>/', views.category, name="category"),
]

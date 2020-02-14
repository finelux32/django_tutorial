from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.readBoard),
    path('articles/', views.articles),
    path('write/', views.writeBoard),
]

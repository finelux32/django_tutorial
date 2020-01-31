from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('restapi_test/', views.restapi_test)
]

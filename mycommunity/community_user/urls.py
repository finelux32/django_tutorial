from django.urls import path

from . import views
from .views import CommunityUserListAPI

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('communityusers/', CommunityUserListAPI.as_view()),
]


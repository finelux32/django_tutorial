from django.urls import path

from . import views
from .views import CommunityUserListAPI, CommunityUserDetailAPI

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('communityusers/', CommunityUserListAPI.as_view()),
    path('communityusers/<int:pk>', CommunityUserDetailAPI.as_view()),
]


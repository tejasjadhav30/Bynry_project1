from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import ProfileView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('submit_success/', views.submit_success, name='submit_success'),
    path('login/', LoginView.as_view(), name='login'),
    #  path('accounts/profile/', ProfileView.as_view(), name='profile'),
]

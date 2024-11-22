from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('', views.PostList.as_view(), name='home'), 
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='nature/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # next_page='home' för omdirigering
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='nature/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='nature/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='nature/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='nature/password_reset_complete.html'), name='password_reset_complete'),
]




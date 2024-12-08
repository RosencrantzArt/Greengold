from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('', views.PostList.as_view(), name='home'), 
    path('posts/', views.PostList.as_view(), name='post_list'), 
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:post_slug>/comment/', views.add_comment, name='add_comment'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:post_slug>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('login/', auth_views.LoginView.as_view(template_name='nature/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='nature/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='nature/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='nature/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='nature/password_reset_complete.html'), name='password_reset_complete'),
]




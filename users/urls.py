from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetView
urlpatterns = [
    
    path('logout/', LogoutView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(),name='register'),
    path('login/', views.MyLoginView.as_view(template_name='users/login.html'),name='login'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html',html_email_template_name = "users/password_reset_email.html"),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('profile/', views.MyProfile.as_view(),name='profile'),
    
]

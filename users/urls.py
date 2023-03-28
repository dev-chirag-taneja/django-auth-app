from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,PasswordResetCompleteView, PasswordResetConfirmView,PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView)

from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    # Authentication
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Account Activation
    path('activate-user/<uidb64>/<token>/', activate_user, name='activate_user'),
    path('generate-link/', generate_link, name='generate_link'),
    
    # Password Change
    path('password-change/', change_password, name='change_password'),
    
    # Password Reset
    path('password-reset/', PasswordResetView.as_view(template_name='reset.html'), name="password_reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
    template_name='reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='reset_complete.html'), name="password_reset_complete"),
]

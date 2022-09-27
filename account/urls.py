from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('setting/', views.UserSettingView.as_view(), name='user_setting'),
    path('email/', views.UserEmailResetView.as_view(), name='email_reset'),
    path('username/', views.UserUsernameResetView.as_view(), name='username_reset'),
    path('reset/', views.UserPasswordResetView.as_view(), name='reset_password'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

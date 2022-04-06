
from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('sign_up/', views.sign_up, name= 'sign_up'),
    path('login_page/', views.login_page, name='login_page'),
    path('profile/', views.edit_profile, name= 'profile'),
    path('logout_user/', views.logout_user, name='logout'),
    path('user/', views.profile, name='user'),
    path('user_other_profile/<username>/', views.user_other_profile, name='user_other'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),
]

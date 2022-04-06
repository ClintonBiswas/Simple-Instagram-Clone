from django.urls import path
from app_post import views

app_name = 'app_post'

urlpatterns = [
    path('',views.homeview, name= 'home'),
]

from django.urls import path,include
from .import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_pass/',views.change_pass,name='change_pass'),
    path('change_pass1/',views.change_pass1,name='change_pass1'),
]
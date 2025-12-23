from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('shop', views.shop,name='shop'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('blog', views.blog,name='blog'),
    path('contact', views.contact,name='contact'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('logout', views.logout,name='logout'),
    path('profile', views.profile,name='profile'),
    path('change-password',views.change_password,name='change-password'),
    path('forgot-password',views.forgot_password,name='forgot-password'),
    path('verify-otp',views.verify_otp,name='verify-otp'),
    path('new-password',views.new_password,name='new-password'),
    
]
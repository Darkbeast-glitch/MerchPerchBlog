from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='home'),
    path('PrivacyPolicy', views.Privacy_Policy, name='privacy_policy'),
    path('AboutMe', views.AboutMe, name='about'),
    path('contactus/', views.Contact, name='contact'),
    path('freegifts/', views.Crypto_stacks, name='freegifts'),


    path('<slug:slug>/', views.post_detail, name='post_detail'),



]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='home'),
    path('PrivacyPolicy', views.Privacy_Policy, name='privacy_policy'),
    path('AboutMe', views.AboutMe, name='about'),
    path('contactus/', views.Contact, name='contact'),
    path('freegifts/', views.Crypto_stacks, name='freegifts'),
    path('Unlocksim/', views.Simlock, name='simlock'),
    path('GiftCard/', views.GiftCardHome, name='GiftCard'),
    path('AmazonCard/', views.AmazonCard, name='AmazonCard'),
    path('EbayCard/', views.EbayCard, name='EbayCard'),
    path('Facebook/', views.Facebook, name='Facebook'),
    path('Googleplay/', views.Googleplay, name='Googleplay'),
    path('Itunes/', views.Itunes, name='Itunes'),
    path('Playstation/', views.Playstation, name='Playstation'),
    path('Steam/', views.Steam, name='Steam'),
    path('Xbox/', views.Xbox, name='xbox'),


    path('<slug:slug>/', views.post_detail, name='post_detail'),



]

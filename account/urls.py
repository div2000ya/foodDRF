from django import urls
from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', SignupAPI.as_view()),
    path('restaurant/',RestaurantDetail.as_view()),
    path('addrestaurant/',AddRestaurant.as_view()),
    path('menu/',MenuDetail.as_view()),
    path('addmenu/',AddMenu.as_view()),
    path('order/',Placeorder.as_view()),
    
]
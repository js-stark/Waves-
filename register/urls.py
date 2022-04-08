from django.urls import URLPattern, path

from register.views import add_cart,remove_cart_item,checkout,razorpaycheck
from .views import *

urlpatterns = [
    path('add_event/<int:product_id>',add_cart,name='add_event'),
    path('',cart,name='register_event'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>',remove_cart_item,name='remove_event_item'),
    path('checkout',checkout,name='checkout'),
     path('proceed-to-pay',razorpaycheck,name='proceed-to-pay'),
]
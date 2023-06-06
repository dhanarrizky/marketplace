from django.urls import path
from . import views as _

urlpatterns = [
    path('', _.index, name='home' ),
    path('category/<int:pk>/',_.filterByCat, name='filter-by-cat'),
    path('cart/<int:pk>', _.cart, name='cart-page'),
    path('cart-update/<int:pk>', _.updatecart, name='cart-page-update'),
    path('add-cart/<int:pk>', _.add_cart, name='add-cart'),
    path('remove-cart/<int:pk>',_.remove_cart, name='remove-cart'),
    path('checkuot/<int:pk>',_.checkout, name='checkout-page'),
    path('send-checkout/<int:pk>', _.send_checkout, name="send-checkout" ),
    path('shop/', _.shop, name='shop-page'),
    path('shop/shortBy/<str:sortby>last-upload', _.shop_sort, name='shop-sort'),
    path('shop/search/', _.shop_search, name="shop-search"),
    path('shop/detail/<str:slug>', _.detail_view, name='detail-page'),
    path('search/', _.search, name='search'),
]

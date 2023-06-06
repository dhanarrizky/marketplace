from django.urls import path
from . import views as _

urlpatterns = [
    path('', _.homeSeller.as_view(), name='seller-home'),
    path('detile-view-seller/<int:pk>', _.detileViewSeller, name='detile-view-seller'),
    path('postProduct/', _.postProduct.as_view() , name="postProduct"),
    # path('requestClient/', _.requestClient.as_view() , name="requestClient"),
    path('requestClient/', _.requestClient, name="requestClient"),
    # path('<int:pk>/detile-client-request/',_.detileReqClient.as_view(), name="detile-client-req"),
    path('<int:pk>/detile-client-request/',_.detileReqClient, name="detile-client-req"),
    path('<int:pk>/profileSeller/', _.profileSeller , name="profileSeller"),
    path('<int:pk>/Delete-produuect/', _.DeleteProduct, name="delete-product"),
    path('<int:pk>/Update-Product/', _.UpdateProduct.as_view(), name="update-product"),
    path('seller/login/', _.loginSeller, name="login-seller"),
    path('seller/logout/', _.logoutSeller, name="logout-seller"),
    path('seller/register/',_.registerSeller, name='register-seller'),
    
]

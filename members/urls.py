from django.urls import path
from .views import login_page, profileView, logout_page, updateProfile, register_page, uploadprofPic

urlpatterns = [
    path('register', register_page, name='register'),
    path('login', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('profile/<int:pk>', profileView, name='profile'),
    path('update/', updateProfile, name='update-profile'),
    path('profile_pic/', uploadprofPic, name="update-profile-pic"),
]

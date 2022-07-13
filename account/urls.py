from django.urls import path
from account import views

app_name = "account"

urlpatterns = [

    path('shopper/register/', views.shopper_registration, name='shopper_registration'),
    #path('shopper/register/', views.shopper_registration, name='shopper-registration'),
    path('seller/register/', views.seller_registration, name='seller_registration'),
    #path('seller/register/', views.seller_registration, name='seller-registration'),
    path('profile/edit/<int:id>/', views.shopper_edit_profile, name='edit-profile'),
    path('login/', views.user_logIn, name='user_logIn'),
    path('logout/', views.user_logOut, name='logout'),
]

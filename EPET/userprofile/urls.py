from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('signup/', views.signup, name='signup'),

    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('my-store/', views.my_store, name='my_store'),
    path('my-store/order-detail/<int:pk>/',
         views.my_store_order_detail, name='my_store_order_detail'),
    path('my-store/add-product/', views.add_product, name='add_product'),
    path('my-store/edit-product/<int:pk>/',
         views.edit_product, name='edit_product'),
    path('my-store/delete-product/<int:pk>/',
         views.delete_product, name='delete_product'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='userprofile/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='userprofile/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='userprofile/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='userprofile/password_reset_complete.html'),
         name='password_reset_complete'),
    path('verify/', views.verification, name='verification'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('product-single/',views.product_single,name='product-single'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'), 
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),    
    path('change-password/',views.change_password,name='change-password'),    
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('new-password/',views.new_password,name='new-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),  
    path('seller-index/',views.seller_index,name='seller-index'),  
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),    
    path('seller-view-product/',views.seller_view_product,name='seller-view-product'),    
    path('seller-formal-shoes/',views.seller_formal_shoes,name='seller-formal-shoes'),    
    path('seller-sports-shoes/',views.seller_sports_shoes,name='seller-sports-shoes'),    
    path('seller-casual-shoes/',views.seller_casual_shoes,name='seller-casual-shoes'),    
    path('seller-all-shoes/',views.seller_all_shoes,name='seller-all-shoes'),    
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),    
    path('seller-product-edit/<int:pk>/',views.seller_product_edit,name='seller-product-edit'),    
    path('seller-product-delete/<int:pk>/',views.seller_product_delete,name='seller-product-delete'), 
    path('product-details/<int:pk>/',views.product_details,name='product-details'),   
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),   
    path('wishlist/',views.wishlist,name='wishlist'),   
    path('remove-from-wishlist/<int:pk>/',views.remove_from_wishlist,name='remove-from-wishlist'), 
    path('add-to-cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),   
    path('cart/',views.cart,name='cart'),   
    path('remove-from-cart/<int:pk>/',views.remove_from_cart,name='remove-from-cart'),   
    path('change-qty/',views.change_qty,name='change-qty'), 
    path('create-checkout-session/', views.create_checkout_session, name='payment'),
    path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'), 
    path('myorder/',views.myorder,name='myorder'),
    path('seller-order/',views.seller_order,name='seller-order'), 
    path('ajax/validate_email/',views.validate_signup,name='validate_email'), 

]








from django.contrib import admin
from django.urls import path,include
from.import views
from django.contrib import admin
from django.conf import settings  
from django.urls import path, include 
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index,name='home'),
   path('shop',views.shop, name='shopgrid'),
   path('shopsingle/<id>',views.shopsingle, name='shopsingle'),
   path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('view_cart/', views.view_cart, name='view_cart'),
   path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
   path('check_out', views.check_out, name='check_out'),
   # path('cart_count/', views.cart_count, name='cart_count')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
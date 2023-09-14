from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *
from pprint import pprint
from .models import Item
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages



def index(request):
    homeitems1=Item.objects.filter(Category_id ='1')
    homeitems2=Item.objects.filter(Category_id ='2')  
    homeitems3=Item.objects.filter(Category_id ='3')
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(user_session=session_key)
    grand_total = 0
    qty=0
    for i in cart_items:
        qty=qty+i.quantity
        grand_total = grand_total + i.product.item_price_offer * i.quantity
    print(grand_total)
        
  
 
    
    return render (request,'shop-home-04.html',{'cart_items': cart_items, 'grand_total': grand_total,'homeitems1':homeitems1, 'homeitems2':homeitems2, 'homeitems3':homeitems3,'qty':qty } )
    
def shop(request):
    homeitemsall=Item.objects.all()
    return render (request,'shop-grid.html',{'homeitemsall':homeitemsall } )

def shopsingle(request,id):
    homeitemssingle=Item.objects.get(id=id)
    homeitemsall=Item.objects.all()
    homeitemsimg=Image.objects.filter(item_id=id)
    return render (request,'shop-single.html',{'homeitemsall':homeitemsall,'homeitemssingle':homeitemssingle,'homeitemsimg':homeitemsimg } )

def add_to_cart(request, product_id):
    product = Item.objects.get(id=product_id)
    session_key = request.session.session_key
    
    if not session_key:
        request.session.save()
        session_key = request.session.session_key
    
    cart_item, created = CartItem.objects.get_or_create(
        product=product, user_session=session_key
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item(s) added to cart successfully")
        response_data = {
        'message': 'Item added to cart successfully',
        'cart_total': CartItem.objects.filter(user_session=session_key).count()
    }
    
    return JsonResponse(response_data)


def view_cart(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(user_session=session_key)
    grand_total = 0
    for i in cart_items:
        
        grand_total = grand_total + i.product.item_price_offer * i.quantity
    print(grand_total)
        
    return render(request,'shop-shopping-cart.html', {'cart_items': cart_items, 'grand_total': grand_total})

def remove_from_cart(request, product_id):
    session_key = request.session.session_key
    delete_items = CartItem.objects.get(id=product_id)
    # grand_total = sum(item.product.price * item.quantity for item in cart_item)
    delete_items.delete()
    cart_items = CartItem.objects.filter(user_session=session_key)
    grand_total = 0
    for i in cart_items:
        grand_total = grand_total + i.product.item_price_offer * i.quantity
    
    response_data = {
        'cart_count': 'cart_count',
        'success': True,
        'message': 'Item removed from cart',
        'grand_total': grand_total,
    }
    return JsonResponse(response_data)



def cart_count(request):
    session_key = request.session.session_key
    cart_count = CartItem.objects.filter(user_session=session_key).count()
    response_data = {
        'cart_count': cart_count,
    }
    return JsonResponse(response_data)

def check_out(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(user_session=session_key)
    grand_total = 0
    for i in cart_items:
        
        grand_total = grand_total + i.product.item_price_offer * i.quantity
    print(grand_total)
        
    return render(request,'shop-checkout.html', {'cart_items': cart_items, 'grand_total': grand_total})
 
   
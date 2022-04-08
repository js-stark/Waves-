from http.client import HTTPResponse
from math import prod
from statistics import quantiles
from django.shortcuts import render,redirect,get_object_or_404
from waves_events.models import Event
from .models import Register
from .models import RegisterItem
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart(request,total=0,quantity=0,cart_items=None):

    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
              cart_items = RegisterItem.objects.filter(user=request.user,is_active=True)
        else:
            cart = Register.objects.get(register_id=_cart_id(request))
            cart_items = RegisterItem.objects.filter(register=cart,is_active=True)
        for cart_item in cart_items:
            total+= (cart_item.event.price * cart_item.quantity)
            quantity += cart_item.quantity
        
        tax = (1 * total) /100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'register_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
    }

    return render(request,'register.html',context)

def add_cart(request, product_id):
    current_user = request.user
    event = Event.objects.get(id=product_id) #get the product
    # If the user is authenticated
    if current_user.is_authenticated:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                # try:
                #     variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                #     product_variation.append(variation)
                # except:
                #     pass


        is_cart_item_exists = RegisterItem.objects.filter(event=event, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = RegisterItem.objects.filter(event=event, user=current_user)
            # ex_var_list = []
            id = []
            for item in cart_item:
                # existing_variation = item.variations.all()
                # ex_var_list.append(list(existing_variation))
                id.append(item.id)

            # if product_variation in ex_var_list:
            #     # increase the cart item quantity
            #     index = ex_var_list.index(product_variation)
            #     item_id = id[index]
            #     item = RegisterItem.objects.get(product=product, id=item_id)
            #     item.quantity += 1
            #     item.save()

            # else:
            item = RegisterItem.objects.create(event=event, quantity=1, user=current_user)
            # if len(product_variation) > 0:
            #     item.variations.clear()
            #     item.variations.add(*product_variation)
            item.save()
        else:
            cart_item = RegisterItem.objects.create(
                event = event,
                quantity = 1,
                user = current_user,
            )
            # if len(product_variation) > 0:
            #     cart_item.variations.clear()
            #     cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('register_event')
    # If the user is not authenticated
    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                # try:
                #     variation = Variation.objects.get(event=event, variation_category__iexact=key, variation_value__iexact=value)
                #     product_variation.append(variation)
                # except:
                #     pass


        try:
            cart = Register.objects.get(register_id=_cart_id(request)) # get the cart using the cart_id present in the session
        except Register.DoesNotExist:
            cart = Register.objects.create(
                register_id = _cart_id(request)
            )
        cart.save()

        is_cart_item_exists = RegisterItem.objects.filter(event=event, register=cart).exists()
        if is_cart_item_exists:
            cart_item = RegisterItem.objects.filter(event=event, register=cart)
            # existing_variations -> database
            # current variation -> product_variation
            # item_id -> database
            # ex_var_list = []
            # id = []
            for item in cart_item:
                # existing_variation = item.variations.all()
                # ex_var_list.append(list(existing_variation))
                id.append(item.id)


            # if product_variation in ex_var_list:
            #     # increase the cart item quantity
            #     index = ex_var_list.index(product_variation)
            #     item_id = id[index]
            #     item = RegisterItem.objects.get(product=product, id=item_id)
            #     item.quantity += 1
            #     item.save()

            
            item = RegisterItem.objects.create(event=event, quantity=1, register=cart)
            # if len(product_variation) > 0:
            #     item.variations.clear()
            #     item.variations.add(*product_variation)
            item.save()
        else:
            cart_item = RegisterItem.objects.create(
                event=event,
                quantity = 1,
                register = cart,
            )
            # if len(product_variation) > 0:
            #     cart_item.variations.clear()
            #     cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('register_event')


def remove_cart_item(request, product_id, cart_item_id):
    event = get_object_or_404(Event, id=product_id)
    if request.user.is_authenticated:
        cart_item = RegisterItem.objects.get(event=event, user=request.user, id=cart_item_id)
    else:
        cart = Register.objects.get(cart_id=_cart_id(request))
        cart_item = RegisterItem.objects.get(event=event, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('register_event')

@login_required(login_url='login')
def checkout(request,total=0,quantity=0,cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
              cart_items = RegisterItem.objects.filter(user=request.user,is_active=True)
        else:
            cart = Register.objects.get(cart_id=_cart_id(request))
            cart_items = RegisterItem.objects.filter(cart=cart,is_active=True)
       
        for cart_item in cart_items:
            total+= (cart_item.event.price * cart_item.quantity)
            quantity += cart_item.quantity
        
        tax = (1 * total) /100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
    }

    return render(request,'waves_store/checkout.html',context)

@login_required(login_url='login')
def razorpaycheck(request):
    registeritems = RegisterItem.objects.filter(user=request.user)
    total_price = 0
    for item in registeritems:
        total_price = total_price + item.event.price * item.quantity

    return JsonResponse({
        'total_price': total_price
    })

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from .forms import OrderForm
import datetime
from .models import Order, Payment, OrderProduct
import json
from waves_events.models import Event
from register.models import RegisterItem
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse


def payments(request):
    print("Inside the payment view")
    
    if request.method == 'POST':
        order = Order.objects.get(user=request.user, is_ordered=False,order_number=request.POST.get('order_number'))
        # Store transaction details inside Payment model
        print("payment model to be formed")
        payment = Payment(
            user = request.user,
            payment_id = request.POST.get('payment_id'),
            payment_method = request.POST.get('payment_method'),
            amount_paid = request.POST.get('amount_paid'),
            status = request.POST.get('status'),
        )
        print("payment model formed")
        payment.save()

        order.payment = payment
        order.is_ordered = True
        order.save()

        print("*******The Order is placed and ordered ********")

        # Move the cart items to Order Product table
        register_items = RegisterItem.objects.filter(user=request.user)

        for item in register_items:
            orderproduct = OrderProduct()
            orderproduct.order_id = order.id
            orderproduct.payment = payment
            orderproduct.user_id = request.user.id
            orderproduct.event_id = item.event_id
            orderproduct.quantity = item.quantity
            orderproduct.event_price = item.event.price
            orderproduct.ordered = True
            orderproduct.save()

            register_item = RegisterItem.objects.get(id=item.id)
            # product_variation = cart_item.variations.all()
            # orderproduct = OrderProduct.objects.get(id=orderproduct.id)
            # orderproduct.variations.set(product_variation)
            orderproduct.save()


            # Reduce the quantity of the sold products
            event = Event.objects.get(id=item.event_id)
            event.stock -= item.quantity
            event.save()

        # Clear cart
        RegisterItem.objects.filter(user=request.user).delete()

        # Send order recieved email to customer
        mail_subject = 'Thank you for your order!'
        message = render_to_string('orders/order_recieved_email.html', {
            'user': request.user,
            'order': order,
        })
        to_email = request.user.email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()

        # Send order number and transaction id back to sendData method via JsonResponse and redirecting user
        print("sent the email")
        context = {
            'order_number': order.order_number,
            'transID': payment.payment_id,
        }
        return JsonResponse(context)

    else:
        print("Somethis went wrong here !")

def place_order(request, total=0, quantity=0,):
    print("Now inside the place order view")
    current_user = request.user

    print(current_user)
    # If the cart count is less than or equal to 0, then redirect back to shop
    register_items = RegisterItem.objects.filter(user=current_user)
    register_count = register_items.count()
    if register_count <= 0:
        return redirect('home')
    
    print(register_count)

    grand_total = 0
    tax = 0
    for register_item in register_items:
        total += (register_item.event.price * register_item.quantity)
        quantity += register_item.quantity
    tax = (1 * total)/100
    grand_total = total + tax

    print(grand_total)

    if request.method == 'POST':
        # Store all the billing information inside Order table
        data = Order()
        print(request.POST.get('first_name'))
        data.user = current_user
        print('user added')
        data.first_name = request.POST.get('first_name')
        print('first name added')
        data.last_name = request.POST.get('last_name')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.roll_number = request.POST.get('roll_number')
        data.date_of_birth = request.POST.get('date_of_birth')
        data.college = request.POST.get('college')
        data.Department = request.POST.get('Department')
        data.year = request.POST.get('year')
        data.referral_code = request.POST.get('referral_code')
        data.order_total = grand_total
        data.payment_mode = request.POST.get('payment_mode')
        print("payment mode added")
        data.razor_payment_id = request.POST.get('payment_id')
        print(request.POST.get('payment_id'))
        data.tax = tax
        data.ip = request.META.get('REMOTE_ADDR')
        print("Gonna save data")
        data.save()
        print("Data saved succesfully")
        # Generate order number
        yr = int(datetime.date.today().strftime('%Y'))
        dt = int(datetime.date.today().strftime('%d'))
        mt = int(datetime.date.today().strftime('%m'))
        d = datetime.date(yr,mt,dt)
        current_date = d.strftime("%Y%m%d") #20210305
        order_number = current_date + str(data.id)
        data.order_number = order_number
        data.save()

        order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)

        print("Printing the order",order)
        context = {
            'user': str(order.user),
            'payment_id': order.razor_payment_id,
            'payment_method': order.payment_mode,
            'amount_paid': order.order_total,
            'status': "succesful",
            'order_number' : order_number,
        }
        print(context)
        return JsonResponse(context)

    else:
        return JsonResponse({
            'context':'Something went wrong here'
        })

def payment_confirmation(request,order_number,transID):
    order = Order.objects.get(user=request.user,order_number=order_number)
    try:
        print("printing products")
        ordered_products = OrderProduct.objects.filter(order_id=order.id)
        subtotal = 0
        for i in ordered_products:
            subtotal += i.event_price * i.quantity

        payment = Payment.objects.get(payment_id=transID)

        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'transID': payment.payment_id,
            'payment': payment,
            'subtotal': subtotal,
        }

        return render(request,'orders/order_complete.html',context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')


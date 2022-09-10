from multiprocessing import context
from tkinter import Text
from django.shortcuts import render,redirect
from django.contrib import messages
import orders
from store.models import Product
from orders.models import Order2,OrderDetails
from django.utils import timezone
from .models import Payment 
from pickle import TRUE
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.
def add_to_cart(request):
    if 'pro_id' in request.GET and 'quantity' in request.GET and 'price' in request.GET and request.user.is_authenticated and not request.user.username=='admin':
        pro_id=request.GET['pro_id']
        quantity=request.GET['quantity']

        order=Order2.objects.all().filter(user=request.user,is_fished=False)
        if not Product.objects.all().filter(id=pro_id).exists:
            return redirect('product')

        product=Product.objects.get(id=pro_id)
        if order:
            old_order=Order2.objects.get(user=request.user,is_fished=False)
            if OrderDetails.objects.all().filter(order=old_order,product=product):
                orderdetails=OrderDetails.objects.get(order=old_order,product=product)
                orderdetails.quantity += int(quantity)
                orderdetails.save()
            else:
                orderdetails=OrderDetails.objects.create(product=product,order=old_order,price=product.price,quantity=quantity)
            messages.info(request,"was added to cart ")

        else:
            new_order=Order2()
            new_order.user=request.user
            new_order.order_date=timezone.now()
            new_order.is_fished=False
            new_order.save()
            orderdetails=OrderDetails.objects.create(product=product,order=new_order,price=product.price,quantity=quantity)
            messages.info(request,"was added to cart ")

        
        return redirect('/%2Fproduct/'+ request.GET['pro_id'])
    return redirect('product')

def cart(request):
    context=None
    if request.user.is_authenticated and not request.user.id==None:
        if Order2.objects.all().filter(user=request.user,is_fished=False):
            order=Order2.objects.get(user=request.user,is_fished=False)
            orderdetails=OrderDetails.objects.all().filter(order=order)
            total=0
            for i in orderdetails:
                total += i.price * i.quantity
            context={
                'order':order,
                'orderdetails':orderdetails,
                'total':total,
            }    
    return render(request,'orders/cart.html',context)


def remove_from_cart(request,orderdetails_id) :
    if request.user.is_authenticated and not request.user.id==None and orderdetails_id:
        orderdetails=OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.order.user.id==request.user.id: #save from  hack
            orderdetails.delete()
    return redirect('cart')   

def add_qty(request,orderdetails_id):
    if request.user.is_authenticated and not request.user.id==None and orderdetails_id:
        orderdetails=OrderDetails.objects.get(id=orderdetails_id)
        orderdetails.quantity +=1
        orderdetails.save()

    return redirect('cart')    
def sub_qty(request,orderdetails_id):
    if request.user.is_authenticated and not request.user.id==None and orderdetails_id:
        orderdetails=OrderDetails.objects.get(id=orderdetails_id)
        if orderdetails.quantity>1:
            orderdetails.quantity -=1
            orderdetails.save()


    return redirect('cart')  

def checkout(request):
    context={}
    adress=request.POST.get('adress')
    phone=request.POST.get('phone')
   

      

    if request.method=='POST' and 'payment' in request.POST:
        if request.user.is_authenticated and not request.user.id==None:
            if Order2.objects.all().filter(user=request.user,is_fished=False):
                order=Order2.objects.get(user=request.user,is_fished=False)
                
                # bill.orderdetails=orderdetails
               
                # print(orderdetails.order.user.username)

                
                payment=Payment()
                payment.order=order
                payment.phone=phone
                payment.adress=adress
                payment.save()
                order.is_fished=True
                a=order
                order.save()
                # print(a)
                # pdf(request)
                messages.info(request,"order is finshed")
        context={
            'adress':adress,
            'phone':phone,

        }
    else:
        if request.user.is_authenticated and not request.user.id==None:
            if Order2.objects.all().filter(user=request.user,is_fished=False):
                order=Order2.objects.get(user=request.user,is_fished=False)
                orderdetails=OrderDetails.objects.all().filter(order=order)
                total=0
                for i in orderdetails:
                    total += i.price * i.quantity
                context={
                    'order':order,
                    'orderdetails':orderdetails,
                    'total':total,
                }
    return render(request,'orders/checkout.html',context)
        


from multiprocessing import context
from django.shortcuts import redirect, render
from . models import Product,Order,UserProfile
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def index(request):
     pro=Product.objects.all()
     context = {'pro':pro}
     return render(request, 'store/index.html', context)
def product(request):
     pro=Product.objects.all()
     name=request.GET.get('productname')
     if name:
          pro=pro.filter(name__icontains=name)
     context = {'pro':pro}
     return render(request, 'store/product.html', context)
def mobile(request):
     pro=Product.objects.filter(category='mobile')
     context = {'pro':pro}
     return render(request, 'store/mobile.html', context)
def laptop(request):
     pro=Product.objects.filter(category='laptop')
     context = {'pro':pro}
     return render(request, 'store/laptop.html', context)
def clothes(request):
     pro=Product.objects.filter(category='clothes')
     context = {'pro':pro}
     return render(request, 'store/clothes.html', context)
def shose_bag(request):
     pro=Product.objects.filter(category='shose_bag')
     context = {'pro':pro}
     return render(request, 'store/shose_bag.html', context)
def details(request,id):
     pro=Product.objects.get(id=id)
     context = {'pro':pro}
     return render(request, 'store/details.html', context)
def profile(request):
     if request.method=='POST':
          messages.info(request,'this is post')
          return redirect('profile')
     else:
          context = {}
          return render(request, 'store/profile.html', context)
def login(request):
	context={}
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		adress=request.POST.get('adress')
		city=request.POST.get('city')
		email=request.POST.get('email')
		username=request.POST.get('username')
		password=request.POST.get('password')
		context={
			'fname':fname,
			'lname':lname,
		    'adress':adress,
			'city':city,
			'email':email,

		}
		if fname and lname and adress and city  and email and username and password :
			if User.objects.filter(username=username).exists():
				messages.info(request,'the user name is taken')
			else:
				if User.objects.filter(email=email).exists():
					messages.info(request,'the Email is taken')
				else:
					# add users
					user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)		
					user.save()
					#add user profile
					userprofile=UserProfile(user=user,adress=adress,city=city)
					userprofile.save()
					messages.info(request,'create acount')
					context={}
					Added=True
		else:
			messages.info(request,'chake empty filed')
		return render(request, 'store/login.html' ,context)
	else:
		return render(request, 'store/login.html',context)

def singup(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
		else:
			messages.info(request,"Eror in passowrd or username")
		return redirect('singup')
	else:
		return render(request, 'store/singup.html')

def profile(request):
	if request.user.username=='admin':
			return redirect('login')
	if request.user.id==None:
		return redirect('profile')
	userinfo=UserProfile.objects.get(user=request.user)
	context={"userinfo":userinfo}
	return render(request, 'store/profile.html',context)
	
def logout(request):
		if request.user.is_authenticated:
			auth.logout(request) 
		return redirect('home')

def like_product(request,idPro):
	if request.user.is_authenticated:
		like_pro=Product.objects.get(id=idPro)
		if UserProfile.objects.filter(user=request.user,like_product=like_pro).exists():
			pass
		else:
			userprofile=UserProfile.objects.get(user=request.user)
			userprofile.like_product.add(like_pro)
	return redirect('details', idPro)

def show_product_like(request):
	context = {}
	if request.user.is_authenticated:
		print("trou")
		userinfo=UserProfile.objects.get(user=request.user)
		pro=userinfo.like_product.all()
		context = {'pro':pro}
	return render(request, 'store/product.html',context)                     
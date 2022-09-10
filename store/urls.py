from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="home"),
	path('product/', views.product, name="product"),
	path('mobile/', views.mobile, name="mobile"),
	path('laptop/', views.laptop, name="laptop"),
	path('clothes/', views.clothes, name="clothes"),
	path('shose-bag/', views.shose_bag, name="shose_bag"),
	path('/product/<int:id>', views.details, name="details"),
	path('login/', views.login, name="login"),
	path('singup/', views.singup, name="singup"),
	path('profile/', views.profile, name="profile"),
	path('logout/', views.logout, name="logout"),
	path('like<int:idPro>', views.like_product, name="like_product"),
	path('show_product_like/', views.show_product_like, name="show_product_like"),
	

]
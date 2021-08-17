from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,ProductAddForm,Order_stock
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Product
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def SignUpAPI(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Created Successfully')
            form.save()
    else:
        form=SignUpForm()
    return render(request,'stock/signup.html',{'form':form})

def LoginAPI(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/detail/')

    else:
        form=AuthenticationForm()
    return render(request,'stock/login.html',{'form':form})

def logoutApi(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def home(request):
    return render(request,'stock/home.html')

""" add the product in to the database """
@login_required(login_url="login/")
def product_add(request):
    if request.method=='POST':
        form=ProductAddForm(request.POST)
        if form.is_valid():
            messages.success(request,'Product is added')
            form.save()
    else:
        form=ProductAddForm()
    return render(request,'stock/stock.html',{'form':form}) 

""" See all the product detail in to the detail.html page """


@login_required(login_url="login/")
def product_detail(request):
    product=Product.objects.all()
    item_name = request.GET.get('name')
    if item_name != '' and item_name is not None:                            
        product =product.filter(name__icontains = item_name)

    paginator = Paginator(product,2)
    page_number = request.GET.get('page')
    product = paginator.get_page(page_number)
    return render(request,'stock/details.html',{'product':product})

"""  product discription detail """


@login_required(login_url="login/")
def product_details(request,id):
    product=Product.objects.filter(id=id)
    return render(request,'stock/detail.html',{'product':product})

""" product purchase detail """


@login_required(login_url="login/")
def busy_stock(request,id):
    obj=Product.objects.filter(id=id)
    if request.method=='POST':
        
        order=Order_stock(request.POST)
        if order.is_valid():
            order.save()

    else:
        order=Order_stock() 
    return render(request,'stock/order.html',{'obj':obj},{'order':order})

def order_detail(request):
    obj=list(Product.objects.all().values_list('name','price'))
    print(obj)


def contect(request):
    return render(request,'stock/contect.html')



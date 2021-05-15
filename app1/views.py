from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app1.models import Product,Order
from app1.form import ProductForm,TakeOrderForm
from user.models import Profile
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    product=Product.objects.all()
    order=Order.objects.all()
    product_count=product.count()
    order_count=order.count()
    staff = Profile.objects.all()
    staff_count = staff.count()
    context={
        "product_count":product_count,
        "order_count":order_count,"staff_count": staff_count,
                }
    return render(request,"app1/index.html",context)

@login_required
def product(request):
    items=Product.objects.all()

    context={
        "items":items

    }
    return render(request,"app1/product.html",context)


def addproduct(request):
    if request.method == "POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_page')

    else:
        form=ProductForm()
    context={
        "form":form,}
    return render(request,"app1/addproduct.html",context)


def updateproduct(request,id):
    item=Product.objects.get(id=id)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect("product_page")
    else:
        form=ProductForm(instance=item)

    context={
        "form": form,
    }

    return render(request,"app1/updateproduct.html",context)

def deleteproduct(request,id):
    item=Product.objects.get(id=id)
    if request.method=="POST":
        item.delete()
        return redirect("product_page")
    context={}
    return render(request, "app1/deleteproduct.html",context)







@login_required
def order(request):
    order = Order.objects.all()
    context={
      "order":order
    }
    return render(request,"app1/order.html",context)




def takeorder(request):
    if request.method=="POST":
        print("hdfue")
        form=TakeOrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect("order_page")
    else:
        form=TakeOrderForm()
    context={
        "form":form
    }
    return render(request,"app1/torder.html",context)

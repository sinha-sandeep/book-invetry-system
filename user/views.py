from django.shortcuts import render,redirect
from user.forms import UserCreation,CreateUserForm,UserProfileForm
from user.models import Profile
from django.contrib.auth.decorators import login_required
from user.models import Profile

# Create your views here.
def register(request):
    if request.method== "POST":
        form=UserCreation(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("index_page")
    if request.method=="POST":
        form1=UserProfileForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect("index_page")
    else:
        form = UserCreation()
        form1= UserProfileForm()
    context={
      "form":form,
        "form1":form1
           }
    return render(request,"authentication/register.html",context)

def profile(request):
    return render(request,"authentication/profile.html",)

def editprofile(request):
    if request.method=="POST":

        form1=CreateUserForm(request.POST,instance=request.user)
        form2=UserProfileForm(request.POST,request.FILES,instance=request.user.profile,)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect("user-profile")
    else:
        form1 = CreateUserForm(instance=request.user)
        form2 = UserProfileForm(instance=request.user.profile)
    context={
        "form1":form1,
        "form2":form2 }
    return render(request,'authentication/editprofile.html',context)


@login_required
def staff(request):
    staff=Profile.objects.all()
    context={"staff":staff,

    }
    return render(request,"authentication/staff.html",context)

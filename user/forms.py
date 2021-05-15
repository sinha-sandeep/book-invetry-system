from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from user.models import Profile
class UserCreation(UserCreationForm):
    email =  forms.EmailField()

    class Meta:
        model= User
        fields=["username",'email',"password1","password2"]



class CreateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields= ["username","email",]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['number',"address",'image']


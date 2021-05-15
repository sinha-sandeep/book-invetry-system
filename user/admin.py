from django.contrib import admin
from user .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['staff','address','number','image']



admin.site.register(Profile,ProfileAdmin)
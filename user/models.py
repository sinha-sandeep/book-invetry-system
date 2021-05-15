from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE,)
    address = models.CharField(max_length=100, null=True)
    number = models.PositiveIntegerField(null=True)
    image = models.ImageField(default="default.jpg",upload_to='profile_images')


    def __str__(self):
        return f'{self.staff.username}-profile'
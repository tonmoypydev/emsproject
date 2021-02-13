from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(blank=True, null=True)
    adress=models.CharField(max_length=250,blank=True,null=True)
    designation=models.CharField(max_length=250,blank=True,null=True)
    date_of_birth=models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.user)
from django.shortcuts import render
from .models import *

# Create your views here.

def user_profile(request):
    user= request.user
    print(user)
    userprofile=UserProfile.objects.get(user=user)
    context={'userprofile':userprofile}
    return render(request,'userprofile.html',context)
   
    

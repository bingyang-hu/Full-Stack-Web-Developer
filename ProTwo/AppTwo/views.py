from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.


def index(request):
    return render(request,"AppTwo/help.html")
def users(request):

    user_list=User.objects.order_by("first_name")
    user_dict={"user":user_list}
    return render(request,'AppTwo/user.html',context=user_dict)

from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.


def index(request):
    return render(request,"AppTwo/help.html")
def users(request):

    # user_list=User.objects.order_by("first_name")
    # user_dict={"user":user_list}
    # return render(request,'AppTwo/user.html',context=user_dict)
    form=NewUserForm()

    if request.method=="POST": #Someone hit submit and sends the information back
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)  # Take back to the home page
        else:
            print('ERROR FORM INVALID')
    return render(request,'AppTwo/user.html',{'form':form})

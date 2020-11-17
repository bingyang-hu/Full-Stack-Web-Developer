from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    my_dict={'insert_me':"Hellow I am from views.py"}
    return render(request,'first_app/index.html',context=date_dict)


#first/index.html 定义了template的位置和名称
# context定义了需要传入文本的上下文。

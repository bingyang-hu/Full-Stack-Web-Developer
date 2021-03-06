from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models  # . means 'look the current directory'
# from django.http import HttpResponse

# Create your views here.



# Class based view CBV

class SchoolListView(ListView):
    context_object_name='schools'
    model =  models.School # It returns a list : school_list;


class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model = models.School
    template_name= 'basic_app/school_detail.html'





# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CLASS BASED VIEWS ARE GREAT!')

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)

        context['injectme']='BASIC INJECTION!'
        return context

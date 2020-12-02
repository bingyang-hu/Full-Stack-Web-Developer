from django.shortcuts import render
from django.views.generic import View,TemplateView
# from django.http import HttpResponse

# Create your views here.



# Class based view CBV

# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CLASS BASED VIEWS ARE GREAT!')

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)

        context['injectme']='BASIC INJECTION!'
        return context

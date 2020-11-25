from django.urls import path
from basic_app import views



#TEMPLAT TAGGING:  equal to application name
app_name='basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),

    # the url for above should be:http://127.0.0.1:8000/basic_app/relative/
    path('other/',views.other,name='other')

]

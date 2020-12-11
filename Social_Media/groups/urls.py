from django.urls import path,include
from . import views

app_names = 'groups'

urlpatterns = [
    path('',views.ListGroups.as_view(),name = 'all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('post/in/(?P<slug>[-\w]+)/',views.SingleGroup.as_view(),name='single'),
    path('join/(?P<slug>[-\w]+)/',veiws.JoinGroup.as_view(),name='join'),
    path('leave/(?P<slug>[-\w]+)/',veiws.LeaveGroup.as_view(),name='leave'),
]

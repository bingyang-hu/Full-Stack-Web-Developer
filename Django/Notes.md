### To activate virtual environment

``` conda info --envs
    activate ****

```

### To create a new project:

``` python

django-admin startproject projectname

```

### To create an application inside this project:

```python

python manage.py startapp Applicationname

```

Application vs. project

A Django **Project** is a collection of applications that when combined together will make up the full web application!
A  Django **App** is created to perform a particular function.


### To register the app (let Django know that we have such an app called ... )

in settings.py: add app name.



### assign urls to this app:

E.g. urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('users/',include('AppTwo.urls')),
]

当根路径为/users时，将该访问发给AppTwo这个App去处理。


而在Apptwo的url.py中：
urlpatterns=[
    path('',views.users,name="users"),

]

当根路径为/users时，调用views中的users函数。


### To create views in views.py

网页都是从view派生来的，每一个view表现为一个简单的python函数。


``` python

from django.shortcuts import render
from django.http import HttpResponse

def users(request):

    user_list=User.objects.order_by("first_name")
    user_dict={"user":user_list}
    return render(request,'AppTwo/user.html',context=user_dict)

```
render函数：将user_dict内容传入到user.html这个模板。



### To Map url.py

from apptwo import views

url('',views.index,name='index'),










# Django框架主要关注的是模型、模板和试图，称为WTV模式。




# When adding apps:
- Tell project that new app is created: add app name into
INSTALLED_APPS in first_project/setting.py
- Create a view in views.py in first_app
- Mapping url from views.py to urls.py in first_project


 Rather than link to urls.py in first_project, link to urls.py in app.



 ### Create a template

 - create new directory 'templatess' (each for each app)

 - Add 'TEMPLATE_DIR' into settings.py (import os,)

 -  Create html file in templates file

 -  render function to



 ### Create a model and then migrate

 ```
 python manage.py migrate

 ```

 ### Then register this change to application

```
python manage.py makemigrations applicationame

```

### To create a superuser for admin interface

Go to admin and Register

then:
```
python manage.py createsuperuser


总的：
1.让project知道app
2.将特定跟路径关联至app urls (project url.py)
3.在app urls中，将url关联至某个view （app url.py)
4.在view中创建函数，提取某些信息from model并导入某个template


## URL Templates Inheritance

Before begin any Django Project, it's always a good idea to sketch out the main idea and organization by hand!

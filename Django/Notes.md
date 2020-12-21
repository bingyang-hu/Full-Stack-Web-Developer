
## No.43 BootStrap Part One - Buttons

## No.44

class='form-group': put spacing between components in the form.

class='form-control':


## No.118

Views should be mapped to a URL in order to be seen.

## No.116
### To activate virtual environment

``` conda info --envs
    activate ****

```
## No.117
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



## No.121 To Map url.py

from apptwo import views

url('',views.index,name='index'),

path('first_app/',include(first_app.urls))

It allows us to look for any url that has the pattern:
wwww.domainname.com/first_app/...

If we match that pattern, the include() function basically tells djangoto go look at the urls.py file inside of first_app folder.



## No.122

TEMPLATE_DIR= '../templates/appname/index.html..'

Template tags:  allow us to inject content into the HTML directly (inject DYNAMIC content that your Django's Apps' VIEWS will produce)

## No.127

A foreign key just denotes that the column coincides with a primary key of another table.

Django create SQL database by:

```
python manage.py migrate
```

Then register the changes to your app by:
```
python manage.py makemigrations yourownappname

```

To create a superuser for admin interface

Go to admin and Register

then:
```
python manage.py createsuperuser
```






## 130. MTV paradigm

 Django framework: model, template and views

 First:  In the views.py file import any models that we will need to use.

 Second: Use the view to query the model for data that we will need

 Third: Pass result from the model to the template

 Fourth: Edit the template so that it is ready to accept and display the data from the model

 Fifth: Map a URL to the view


## 137. Model Forms

purpose: Grab information from the user's form and save it to a model. In the previous session, we only grab the information from form and did NOT save them to the model.

Meta class  : provide information connecting the model to the form

```
class MyNewForm(forms.ModelForm) : # rather than forms.Form
  class Meta # Connect model to the form
    model = MyModel
    fields= ..
```















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


## No.141 Relative URLs Coding Examples


## No.142 URL Template Inheritance



Before begin any Django Project, it's always a good idea to sketch out the main idea and organization by hand!

base.html:

```
<body>
 {% block body_block %}

 {% endblock %}

</body>

```

other.html
```
<!DOCTYPE html> #this line is necessary!
{% extends "basic_app/base.html" %}  # Remember that the TEMPLATE_DIR is to '../templates'?

{% block body_block %} # 'body_block' is just a name and you can change

<HTML specific for other.html>
<HTML specific for other.html>

{% endblock %}

```


## 148.Django Password:

difference with folder 'static' and file 'media':

static: store files you provide
media: store files the users provide


## 156. Setting Up Github

Git: a version control system that helps keep track of changes in your code

Github: a company and web that helps manage git and hosts your files on their site


## No.161 Detail View and List View

Connect view and template and model: list the records from  the models
or show details of a single record.

## 178. Social Clone Part Three

from django.contrib.auth import views as auth_views

Its goal is to use Django's own view: login and logout view, rather than cearting them by yourself.

## 187 Debug

## Tortued by slug:::

The problem I found:

In Group-detail.html, it should be 'slug = group.slug' rather than 'groupS.slug'

In Group_list.html, it should be  slug =group.slug rather than groupS.slug.


## 189.
To get the debug toolbar, in your virtual environment use:

```
 pip install django-debug-toolbar
```

## Changes with regard to different version of Django:

- resolvers:
  - current: Django.urls import reverse
  - previous:

- regular expression in path:
  - current: path('by/<str:username>/<str:pk>',views.PostDetail.as_view(),name='single')
  - prev: url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views....')

- reverse_lazy
  - cur: from django.urls import rever_lazy
  - prev: from django.core.urlresolvers import reverse_lazy


- load staticfiles
  - cur: {% load static %}
  - prev: {% load staticfiles %}





总的：
1.让project知道app
2.将特定跟路径关联至app urls (project url.py)
3.在app urls中，将url关联至某个view （app url.py)
4.在view中创建函数，提取某些信息from model并导入某个template

include(list,app_name),namespace=None. Don't write include(list,app_name= ...),no 'app_name':
path('posts/',include(('posts.urls','posts'),namespace='posts')),
path('groups/',include(('groups.urls','groups'),namespace='groups')),

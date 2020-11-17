#create a new project:
django-admin startproject projectname
# create a simple application
python manage.py startapp appname

#To run the server
python manage.py runserver


#  Application vs. project

A Django Project is a collection of applications that when combined together will make up the full web application!
A  Django App is created to perform a particular function.


# Django框架主要关注的是模型、模板和试图，称为WTV模式。




# When adding apps:
1. Tell project that new app is created: add app name into
INSTALLED_APPS in first_project/setting.py
2. Create a view in views.py in first_app
3. Mapping url from views.py to urls.py in first_project


 # Rather than link to urls.py in first_project, link to urls.py in app.



 # Create a template

 1. create new directory 'templatess' (each for each app)

 2. Add 'TEMPLATE_DIR' into settings.py (import os,)

 3. Create html file in templates file

 4. render function to **sss**



 '''
 Hey is the notes?

 '''
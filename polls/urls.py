from django.urls import path
from . import views

app_name = 'polls' #Add namespace to the URLconf
#If you have multiple apps which can have view functions with the same name,
#then in order to refer to a particular url/route from WITHIN a template,
#we need to be able to differentiate between the views with the same name.
#This is done with namespacing i.e. adding an app_name variable in the app level urls.py
#and also adding <app_name> : route name in the url template tag in the template

urlpatterns = [
path('', views.index, name = 'index'),
path('<int:question_id>/', views.detail, name = 'detail'),
path('<int:question_id>/results/', views.results, name = 'resultwa'),
path('<int:question_id>/vote/',views.vote, name = 'vote'),
]
#The name argument serves as an alias for the route url so that when 
#a url has to be written in a template, it doesnt need to be hard-coded
#i.e. we wont need to write: path/<arg>/ but can just use the value of
#the name variable to refer to that route.


#The part between the angular brackets< > is captured as argument, and then passed
#to the matched view function.

#A view function must return either an HttpResponse object or an exception


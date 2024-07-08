from django.urls import path
from . import views
urlpatterns=[
 path("",views.index),
 path("<int:myMonth>",views.monthNum),
 path("<str:myMonth>",views.month,name="mon"),
 
]
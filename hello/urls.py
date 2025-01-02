from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"), # http://127.0.0.1:8000/hello/
    path("mom",views.mom, name="mom"), # http://127.0.0.1:8000/hello/mom,
    path("<str:name>",views.greet,name="greet") # http://127.0.0.1:8000/hello/ryan
]
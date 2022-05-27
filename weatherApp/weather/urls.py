from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(
        r'^weather(?:city=(?P<city>/^[A-Za-z]+$/)?:country(?P<country> /^[a-z]+$/))?$', views.index)
]

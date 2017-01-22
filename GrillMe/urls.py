"""Grill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from GrillMe import views

urlpatterns = [
    url(r'^list/$', views.FoodList.as_view(), name='food_list'),
    url(r'^new/$', views.FoodCreate.as_view(), name='food_new'),
    url(r'^edit/(?P<pk>\d+)$', views.FoodUpdate.as_view(), name='food_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.FoodDelete.as_view(), name='food_delete'),
    url(r'^$', views.Index.as_view(), name='index'),
]
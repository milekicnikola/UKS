from django.conf.urls import patterns, url

from uksApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
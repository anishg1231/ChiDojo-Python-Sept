from django.conf.urls import url
# from django.contrib import admin
from.import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^quotes$', views.quotes),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^logout$', views.logout),

]

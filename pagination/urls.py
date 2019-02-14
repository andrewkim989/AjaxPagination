from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^createuser$', views.create),
    url(r'^users/(?P<num>\d+)$', views.users)
]
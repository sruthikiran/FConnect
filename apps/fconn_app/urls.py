from django.conf.urls import url
from . import views

# app_name = 'fconn_app'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$',views.signin,name='signin'),
    url(r'^logval$',views.logval,name='logval'),
    url(r'^dashboard$',views.dashboard,name='dashboard'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^addCollege$',views.addCollege),
    url(r'^userInfoVal$',views.userInfoVal),
    url(r'^resources$',views.resources),
    url(r'^checklist\/(?P<number>\d+)$',views.checklist),
    url(r'^updatechecklist\/(?P<number>\d+)$',views.updatechecklist),
    url(r'^logout$',views.logout)
]

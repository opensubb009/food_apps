from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from . import views

app_name = "apps.login"

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^change_password$', views.change_password, name='change_password'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^signup/validate_username/$', views.validate_username, name='validate_username'),
]

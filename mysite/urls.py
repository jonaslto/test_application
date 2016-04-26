from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import SignUpView, LoginView, HomePageView, LogoutView, SendPageView, OutPageView, SendConfirmPageView
from mysite import views as mysite_views

admin.autodiscover()

urlpatterns = [
    url(r'^talks/', include('talks.urls', namespace='talks')),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^out/$', OutPageView.as_view(), name='out'),
    url(r'^send_done/$', SendPageView.as_view(), name='send'),
	url(r'^form/$', mysite_views.get_name, name='form'),
    url(r'^send_confirm/$', SendConfirmPageView.as_view(), name='sendconf'),

]
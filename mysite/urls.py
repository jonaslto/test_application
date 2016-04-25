from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import SignUpView, LoginView, HomePageView, LogoutView, SendPageView, OutPageView, SendConfirmPageView

admin.autodiscover()

urlpatterns = [
    url(r'^talks/', include('talks.urls', namespace='talks')),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^accounts/logout/$', 'mysite.views.logout_page', name='logout2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^out/$', OutPageView.as_view(), name='out'),
    url(r'^send_done/$', SendPageView.as_view(), name='send'),
    url(r'^logout/$', 'mysite.views.logout_page'),
    url(r'^form/$', 'mysite.views.get_name', name='form'),
    url(r'^send_confirm/$', SendConfirmPageView.as_view(), name='sendconf'),

]
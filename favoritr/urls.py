"""favoritr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pages.views import main_page, login_page, register_page, control_panel, mylistpage,notfound, deleter, deleter2
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy

urlpatterns = [

	url(r'^$', main_page, name = 'home'),
    url(r'^user/(?P<username>\w+)/list/(?P<slug>[-\w]+)/delete/$', deleter),
    url(r'^user/(?P<username>\w+)/list/(?P<slug>[-\w]+)/deleteitem/(?P<pk>[\d]+)', deleter2),
    url(r'^notfound$', notfound, name = 'notfound'),
	url(r'^login/$', login_page, name='login'),
    url(r'^user/(\w+)/profile/$', control_panel, name='profile'),
    url(r'^user/(?P<username>\w+)/list/(?P<slug>[-\w]+)/$', mylistpage, name='lists'),
    url(r'^register/$', register_page, name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {
        "next_page" : reverse_lazy('home')
        }, name="logout"),
    url(r'^static(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
    url(r'^media(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

] 

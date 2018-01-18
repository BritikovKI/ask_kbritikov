"""ask_kbritikov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from ask_app.views import *

urlpatterns = [
#    url(r'modal',mod_log),
    url(r'scroll',scroll,name='scroll'),
    url(r'like',like,name='like'),
    url(r'^vote/&', vote,name='vote'),
    url(r'^author$',profile,name='author'),
    url(r'^log_out/?', exit,name="lo"),
    url(r'^admin/?', admin.site.urls,name='admin'),
    url(r'^auth$', log, name='auth'),
    url(r'^$', main_new , name='main'),
    url(r'^tag$', Tagged.as_view(),name='tag'),
    url(r'^debate$', Debate,name='deb'),
    url(r'^question', Discussion,name='disc'),
    url(r'^reg', Registration,name='reg'),
    url(r'^set', Settings,name='settings'),
    url(r'^hot', Hot,name='hot'),
#    url(r'^myModal',modal)
]

"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

import contacts.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list'),
    url(r'^new/$', contacts.views.CreateContactView.as_view(), name='contacts-new'),
    url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contacts-edit'),
    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(), name='contacts-delete'),
    url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(), name='contacts-view'),
    url(r'^edit/(?P<pk>\d+)/addresses/$', contacts.views.EditContactAddressView.as_view(), 
            name='contacts-edit-addresses'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
]

urlpatterns += staticfiles_urlpatterns()


"""project_story_blog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from core.views import *

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^$', main_page),
    url(r'^registration/$', registration_page),
    url(r'^account/(?P<name_of_user>\w+)/$', account_page),
    url(r'^users_list/$', users_list_page),
    url(r'^blogs_list/$', blog_list_page),
    url(r'^account/(?P<name_of_user>\w+)/(?P<name_of_blog>\w+)/$', user_blog_page),
    url(r'^account/(?P<name_of_user>\w+)/(?P<name_of_blog>\w+)/post_(?P<post_id>\d+)/$', user_blog_post_page),
]

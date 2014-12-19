from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^(.+)$', 'swag.views.map_view'),
    url(r'^$', 'swag.views.map_list'),
)

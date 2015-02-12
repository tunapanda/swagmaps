from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swag_devsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('proxy/(?P<url>.*)', 'proxy.views.proxy_view'),
    url(r'^xapi_proxy/', include('xapi_proxy.urls', namespace="xapi_proxy")),
    url(r'^', include('swag.urls')), 
)

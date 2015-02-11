from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'dummy', 'xapi_proxy.views.dummy_response', name="dummy"),
    url(r'^(.*)$', 'xapi_proxy.views.main', name="main"),
    url(r'', 'xapi_proxy.views.main', name="main"),
)

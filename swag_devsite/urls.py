from django.conf.urls import patterns, include, url
from django.contrib import admin
import swag.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swag_devsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(swag.urls)),
)

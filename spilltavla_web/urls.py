from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', 'spilltavla_web.views.frontpage', name='frontpage'),
    # Examples:
    # url(r'^$', 'spilltavla_web.views.home', name='home'),
    # url(r'^spilltavla_web/', include('spilltavla_web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEVELOPMENT:
    urlpatterns += staticfiles_urlpatterns()

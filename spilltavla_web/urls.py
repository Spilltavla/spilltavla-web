from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


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

    #Handling user registration, login and logout
    url(r'^login/?$', 'user_management.views.login_page'),
    url(r'^login/error/$', 'user_management.views.login_error',
        name='login_error'),
    url(r'login/', include('social_auth.urls')),
    url(r'^user_registration/$', 'user_management.views.user_registration',
        name='user_registration'),
    url(r'^logout/$', 'user_management.views.logout', name='logout'),

)

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from incidencias.frontend.views import loginView, registro, pagina, index, logoutView

urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^login$',loginView),
    url(r'^logout$',logoutView),
    url(r'^registro$',registro),
    url(r'^pagina$',pagina),
    # Examples:
    # url(r'^$', 'incidencias.views.home', name='home'),
    # url(r'^incidencias/', include('incidencias.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

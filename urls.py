from django.conf.urls.defaults import *
from django.conf import settings
import django.contrib.auth.views
from django.contrib import admin
import os
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	# EgPlus: -----------------------------------------------------------------------------------------------------

	(r'','sistema.views.home'),
	(r'^egplus/$','sistema.views.egplus'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    # importando o template -------------------------------------------------------------------------------------

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.getcwd(),'static') }),
)

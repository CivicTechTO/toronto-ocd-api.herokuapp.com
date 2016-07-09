from django.conf.urls import patterns, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   ('', include('boundaries.urls')),
   ('', include('imago.urls')),
   # ('', include('locksmith.auth.urls')),
   (r'^admin/', include(admin.site.urls)),
)

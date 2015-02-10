from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'PaleoSites.views.home', name='home'),
    url(r'^index', 'PaleoSites.views.home', name='home'),
    url(r'^kml/', 'PaleoSites.views.all_kml', name='all_kml'),
    url(r'^map/', 'PaleoSites.views.map_page', name='map_page'),
)

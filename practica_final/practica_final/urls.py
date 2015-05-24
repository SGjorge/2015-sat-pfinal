from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practica_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin', include(admin.site.urls)),
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^actividad/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_URL2}),
    url(r'^actividad/(\d+)', 'app.views.activity'),
    url(r'^ayuda', 'app.views.help'),
    url(r'^add', 'app.views.addActivity'),
    url(r'^moreOne', 'app.views.moreOne'),
    url(r'^preferences', 'app.views.savePreferences'),
    url(r'^$', 'app.views.index'),
    url(r'^login', 'app.views.login'),
    url(r'^update', 'app.views.up'),
    url(r'^usuarios', 'app.views.usuarios'),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_URL2}),
    url(r'^RSS$', 'app.views.RSSMain'),
    url(r'^todas$', 'app.views.allActivities'),
    url(r'^(.*)/RSS', 'app.views.RSS'),
    url(r'^(.*)', 'app.views.users'),
)

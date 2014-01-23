from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/$', 'users.views.front'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_user/$', 'users.views.create_user'),
    url(r'^user/(?P<user_id>\d+)/$', 'users.views.edit_user'),
    url(r'^delete_user/(?P<user_id>\d+)/$', 'users.views.delete_user'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,
			'show_indexes':True}),
)

urlpatterns += staticfiles_urlpatterns()
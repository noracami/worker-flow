from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'workerflow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'worker.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^worker/', include('worker.urls', namespace="worker")),
)

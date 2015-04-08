from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('blog.urls')),
)

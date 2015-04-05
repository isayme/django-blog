from django.conf.urls import patterns, url

from blog import views
from blog.feed import RssPostFeed, AtomPostFeed

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^rss/$', RssPostFeed(), name='rss'),
    url(r'^atom/$', AtomPostFeed(), name='atom'),
    url(r'^page/(?P<page_num>\d+)/$', views.page, name='page'),
    url(r'^category/(?P<category>\w+)/$', views.category, name='category'),
    url(r'^category/(?P<category>\w+)/page/(?P<page_num>\d+)/$', views.category, name='category'),
    url(r'^tag/(?P<tag>\w+)/$', views.tag, name='tag'),
    url(r'^tag/(?P<tag>\w+)/page/(?P<page_num>\d+)/$', views.tag, name='tag'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<path>\S+)', views.post, name='post'),
)

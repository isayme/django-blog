# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from blog.models import Post

class RssPostFeed(Feed):
    title = u'独语者'
    link = '/blog/'
    description = 'Think Before Speak'

    def items(self):
        return Post.objects.all()[:10]

    def item_link(self, post):
        link_attr = [
            '/blog',
            str(post.publish_time.year),
            str(post.publish_time.month),
            post.slug
        ]
        return '/'.join(link_attr)

class AtomPostFeed(RssPostFeed):
    feed_type = Atom1Feed
    subtitle = RssPostFeed.description
    
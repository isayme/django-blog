from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tag Name')
    description = models.CharField(max_length=144, default='')

    def __unicode__(self):
        return '%s' % self.name
    __str__ = __unicode__

    @models.permalink
    def get_absolute_url(self):
        return ('tag', (), {
                'tag': self.name,
            })

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Category Name')
    description = models.CharField(max_length=144, default='')

    def __unicode__(self):
        return '%s' % self.name
    __str__ = __unicode__

    @models.permalink
    def get_absolute_url(self):
        return ('category', (), {
                'category': self.name,
            })

class PostImage(models.Model):
    image = models.ImageField(null=True)

    def thumb(self):
        return u'<a href="{0}"><img src="{0}" /></a>'.format(self.image.url)
    thumb.allow_tags = True
    thumb.short_description = 'Thumbnail'

@receiver(pre_delete, sender=PostImage)
def post_image_delete(sender, instance, **kwargs):
    instance.image.delete(False)

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tag')

    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=100, unique=True)

    content = models.TextField()

    def __unicode__(self):
        return '%s' % self.title
    __str__ = __unicode__

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {
                'year': self.publish_time.year,
                'month': self.publish_time.month,
                'path': self.slug,
            })

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-publish_time"]

import logging
from django.conf import settings
from django_comments.signals import comment_will_be_posted
from django_comments.models import Comment
from django.db.models.signals import pre_save
from trie import Trie

spamTrie = Trie()

class Spam(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Spam Keyword', null=True)
    description = models.CharField(max_length=144, default='', null=True)

    def __unicode__(self):
        return '%s' % self.name
    __str__ = __unicode__

@receiver(pre_save, sender=Spam)
def spam_save(sender, instance, **kwargs):
    logging.debug('Spam insert key: %d', instance.name)
    spamTrie.insert(instance.name)

@receiver(pre_delete, sender=Spam)
def spam_delete(sender, instance, **kwargs):
    logging.debug('Spam delete key: %d', instance.name)
    spamTrie.delete(instance.name)

spamwords = Spam.objects.all()
for key in spamwords:
    spamTrie.insert(key.name)

def spam_check(sender, comment, request, **kwargs):
    word = comment.comment

    while word:
        logging.debug('Spam check key: %d', word)
        if spamTrie.match(word):
            comment.is_public = False
            break

        word = word[1:]

    return True

comment_will_be_posted.connect(spam_check, sender=Comment, dispatch_uid="comment_spam_check_akismet")

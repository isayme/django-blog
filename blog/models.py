from django.db import models
from django.contrib.auth.models import User

#from django_qiniu.fields import QiniuFileField

#def qiniu_key_maker_user_image(instance, filename):
#    pass

#class QiniuImage(models.Model):
#    qiniu_file = QiNiuFileField(upload_to=qiniu_key_maker_file, null=True)
#    qiniu_image = QiNiuImageField(upload_to=qiniu_key_maker_image, null=True)

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

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tag')

    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=100, unique=True)

    content = models.TextField()
    #image = models.ImageField(upload_to='images/')

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

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField(max_length=144)
    publish_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True)

    def __unicode__(self):
        return '%s' % self.content
    __str__ = __unicode__


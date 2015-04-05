from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

from blog.models import Post, Category, Tag, Comment

class PostAdmin(MarkdownModelAdmin):
    list_display = ('title', 'publish_time')
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {"description": ("name",)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {"description": ("name",)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)

from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

from blog.models import Post, Category, Tag, PostImage, Spam

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('thumb',)

class PostAdmin(MarkdownModelAdmin):
    list_display = ('title', 'publish_time')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

    def get_changeform_initial_data(self, request):
        return {'author': request.user}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'description': ('name',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'description': ('name',)}

# Register your models here.
admin.site.register(PostImage, PostImageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Spam)

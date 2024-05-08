from django.contrib import admin
from .models import Comment, Tag, Author, About, Post, SocialMedia
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author',)
    list_display_links = ('id', 'title', 'author',)
    filter_horizontal = ('tags',)
    list_filter = ('author',)
    search_fields = ('id', 'title', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'occupation')
    list_display_links = ('id', 'name', 'occupation')
    filter_horizontal = ('social_media', )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)
admin.site.register(About)
admin.site.register(SocialMedia)

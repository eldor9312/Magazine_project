from django.contrib import admin
from .models import Post, Author, Category, Comment, PostCategory
from modeltranslation.admin import TranslationAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ['heading','author']
    list_filter = ['post_category','author']


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin2(TranslationAdmin):
    model = Post

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)

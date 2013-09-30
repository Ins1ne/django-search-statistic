# coding: utf-8
from django.contrib import admin
from example.models import Article


class ArticleAdmin(admin.ModelAdmin):

    search_fields = ['title']
    list_display = ('title', 'timestamp')


admin.site.register(Article, ArticleAdmin)

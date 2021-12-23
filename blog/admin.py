from django.contrib import admin
from blog.models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_filter = [
         "tags"
    ]

admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    # tuple中只有一个元素时要加一个逗号.
    list_filter = ('pub_time',)

admin.site.register(models.Article,ArticleAdmin)
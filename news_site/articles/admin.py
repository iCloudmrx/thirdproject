from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)


@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'body', 'date']

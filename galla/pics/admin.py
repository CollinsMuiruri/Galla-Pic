from django.contrib import admin
from .models import Editor,Article,tags,Location,Category

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(Location)
admin.site.register(Category)

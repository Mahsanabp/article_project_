from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "rate", "date", "link", "image")
    fieldsets = (
        ("name", {"fields" : ("name",)}),
        ("rate", {"fields" : ("rate",)}),
        ("date", {"fields" : ("date",)}),
        ("link", {"fields" : ("link",)}),
        ("images", {"fields" : ("image",)})
        
    )



admin.site.register(Article, ArticleAdmin)
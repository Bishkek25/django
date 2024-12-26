from django.contrib import admin
from posts.models import Post, Category, Tag

# @admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    List_display = ("title", "description", "rate", "created_date", "updated_date")
    list_filter = ("created_date", "updated_date", "category")




admin.site.register(Category)
admin.site.register(Tag)

from django.contrib import admin
from posts.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "rate", "created", "updated")
    list_filter = ("created", "updated", "catergory")
    search_fields = ("title", "description")
    list_editable = ("rate",)

admin.site.register(Category)
admin.site.register(Tag)

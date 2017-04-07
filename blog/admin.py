from django.contrib import admin

# Register your models here.

from .models import Post

#@admin.register(Post)

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Blog Post Details",{"fields": ["title", "author","createdDate","publishedDate","uid"]}),
        ("Blog Post",{"fields": ["text"]})
    ]

    list_display=("title","author","createdDate","publishedDate","uid")
    list_display_links=("title","uid")
    search_fields=("title","author","uid","text")

admin.site.register(Post, BlogAdmin)

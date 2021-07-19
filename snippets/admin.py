from django.contrib import admin
from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = [
        'created',
        'title',
        'code',
        'linenos',
        'language',
        'style',
    ]
    list_display_links = [
        'created',
        'title',
    ]
    search_fields = [
        'title',
        'code',
        'language',
        'linenos',
    ]
admin.site.register(Snippet, SnippetAdmin)
from django.contrib import admin

# Register your models here.

from .models import Artist

# More additional information for admin area


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'list_date',
                    'agent', 'city', 'is_published')
# Clickable title on admin (tuple for Python)
    list_display_links = ('title',)
# List Filter by agent
    list_filter = ('agent'),
# Publishing and Unpublished by click
    list_editable = ("is_published"),
# Search Fields (top search bar)
    search_fields = ("title"),
# Pagination
    list_per_page = 25


admin.site.register(Artist, ArtistAdmin)

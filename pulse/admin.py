from django.contrib import admin
from .models import Pulse

class PulseAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'artist', 'get_view_count', 'get_like_count', 'release_date')

    # Fields to filter the list by
    list_filter = ('release_date',)

    # Fields to search by
    search_fields = ('title', 'artist__username')

    # Fields to be edited inline
    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'duration', 'release_date', 'description')
        }),
        ('Media', {
            'fields': ('video',)
        }),
    )

    # Method to get view count
    def get_view_count(self, obj):
        return obj.views.count()
    get_view_count.short_description = 'Views'

    # Method to get like count
    def get_like_count(self, obj):
        return obj.likes.count()
    get_like_count.short_description = 'Likes'

admin.site.register(Pulse, PulseAdmin)

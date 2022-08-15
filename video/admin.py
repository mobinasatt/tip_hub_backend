# Django packages
from django.contrib import admin
# Third party apps
from mptt.admin import DraggableMPTTAdmin
# Local apps
from .models import Video, Category


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('master', 'views', 'created')
    list_filter = ('master', 'created', 'updated')
    search_fields = ('description', 'about_video')
    raw_id_fields = ('master',)
    prepopulated_field = {'slug': ('title',)}


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_field={'slug': ('name',)}
)

# Django packages
from django.contrib import admin
# Third party apps
from mptt.admin import DraggableMPTTAdmin
# Local apps
from . import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('master', 'views', 'jalali_date')
    list_filter = ('master', 'created', 'updated')
    search_fields = ('description', 'about_video')
    raw_id_fields = ('master',)
    prepopulated_field = {'slug': ('title',)}


admin.site.register(
    models.Category,
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

admin.site.register(
    models.Comment,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'jalali_date')
    list_filter = ('user', 'created')
    search_fields = ('user', 'video')

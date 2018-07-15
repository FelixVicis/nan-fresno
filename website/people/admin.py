from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import People


class peopleAdmin(admin.ModelAdmin):
    search_fields = ('firstName', 'lastName', 'firstName', 'lastName')
    list_display = ('firstName', 'lastName', 'city', 'state', 'hyperlink')
    list_display_links = ('firstName', 'lastName')
    list_filter = ('age', 'height', 'weight', 'state', 'county', 'created_at')
    search_fields = ('firstName', 'lastName', 'city', 'state',
                     'county', 'circumstance', 'age', 'sex',
                     'race', 'eye_color', 'hair_color', 'weight',
                     'height')

    def hyperlink(self, obj):
        pk = obj.pk
        return format_html('<a href="/people/details/%d"> View Person </a>' % pk)


admin.site.register(People, peopleAdmin,)

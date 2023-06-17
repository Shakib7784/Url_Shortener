from django.contrib import admin

from .models import ShortLink

@admin.register(ShortLink)
class ShortLinkClass(admin.ModelAdmin):
    list_display=["id","created","long_url","short_url","last_accessed","times_followed"]


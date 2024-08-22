from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Remixed Lyrics Admin Portal"
admin.site.site_title = "Remixed Lyrics Admin Portal"
admin.site.index_title = "Remixed Lyrics"

admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(RemixLevel)

# class RemixLevelAdmin(admin.ModelAdmin):
#     list_display = ('level') 
# admin.site.register(RemixLevel, RemixLevelAdmin)

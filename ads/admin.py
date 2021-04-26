from django.contrib import admin
from ads.models import Ad, Comment

class AdAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')

admin.site.register(Comment, AdAdmin)

from django.contrib import admin
from .models import SchedulePost, PlatformAuth

# admin.site.register(Platform)
admin.site.register(PlatformAuth)
admin.site.register(SchedulePost)

from django.contrib import admin
from .models import Load, Location, LoadStatus

admin.site.register(Load)
admin.site.register(Location)
admin.site.register(LoadStatus)
import datetime

from django.contrib import admin
from .models import *


class GraphicAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.create_graphic()
        obj.date = datetime.datetime.now()
        obj.save()


admin.site.register(Graphic, GraphicAdmin)

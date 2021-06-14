from django.contrib import admin
from .models import *

from .main_tasks import create_task


class GraphicAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        create_task(obj)
        obj.date = datetime.datetime.now()
        obj.save()


admin.site.register(Graphic, GraphicAdmin)

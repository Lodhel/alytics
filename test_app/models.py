import numpy as np
from django.db import models
import datetime

from .graphic import GraphicMixin


class Graphic(GraphicMixin, models.Model):
    func = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True)
    t_days = models.IntegerField()
    t_hours = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now())
    text_status = models.TextField(null=True, blank=True)

    def create_graphic(self):
        _image = self.create(x=np.linspace(-40, 40, 10000), y=self.func)
        self.image = _image
        self.save()

    def count_t(self):
        return [datetime.datetime.now() - datetime.timedelta(days=self.t_days), datetime.datetime.now()]

    class Meta:
        db_table = "graphics"
        verbose_name = 'graphic'
        verbose_name_plural = 'graphics'

    def __str__(self):
        return str(self.pk)

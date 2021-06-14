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
        try:
            _image = self.create(x=self.t_days, y=self.func)
            self.image = _image
        except Exception as ex:
            self.text_status = str(ex)

        self.save()

    class Meta:
        db_table = "graphics"
        verbose_name = 'graphic'
        verbose_name_plural = 'graphics'

    def __str__(self):
        return str(self.pk)

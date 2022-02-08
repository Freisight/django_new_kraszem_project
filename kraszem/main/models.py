from django.db import models

# Create your models here.
from django.urls import reverse


class Cottage(models.Model):
    COMM = [
        (1, 'Электричество'),
        (2, 'Газ'),
        (3, 'Вода'),
        (4, 'Интернет')
    ]

    DIRECT = [
        (1, 'Симферопольское шоссе'),
        (2, 'Новорязанское шоссе'),
        (3, 'Калужское шоссе'),
        (4, 'Новорижское шоссе')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(max_length=None)
    min_size = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    commumication = models.PositiveSmallIntegerField(choices=COMM)
    direct = models.PositiveSmallIntegerField(choices=DIRECT)
    main_photo = models.ImageField(upload_to='main_photos/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cottage', kwargs={'cottage_id': self.pk, 'direct': self.direct})
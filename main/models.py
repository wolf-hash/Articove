from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver


def path_and_rename(instance, filename):
    upload_to = 'products/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)

        return os.path.join(upload_to, filename)

class Product(models.Model):
    name        = models.CharField(default='', max_length=100, primary_key=True)
    desc        = models.TextField(default='', max_length=1000)
    image       = models.ImageField(upload_to=path_and_rename, default='', blank=True)
    price       = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Product)
def submission_delete_logo(sender, instance, **kwargs):
    instance.image.delete(False)
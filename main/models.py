from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from accounts.models import UserAccount


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

class Cart(models.Model):
    user        = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    count       = models.PositiveIntegerField(default=0)
    total       = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "User: {} has {} items in their cart. Total = Rs.{}".format(self.user, self.count, self.total)

class Entry(models.Model):
    product     = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    Cart        = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField(null=True)
    
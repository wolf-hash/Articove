# Generated by Django 3.0.8 on 2020-11-30 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Product'),
        ),
    ]

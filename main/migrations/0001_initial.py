# Generated by Django 3.0.8 on 2020-11-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('name', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('desc', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
# Generated by Django 4.0 on 2021-12-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='description',
            field=models.TextField(max_length=255, null=True, verbose_name='Description'),
        ),
    ]

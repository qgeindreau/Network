# Generated by Django 3.0 on 2021-12-19 15:01

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211219_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(default=2),
            preserve_default=False,
        ),
    ]
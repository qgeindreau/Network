# Generated by Django 4.0 on 2021-12-19 22:55

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_user_bio_alter_user_facebook_account_and_more'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='notebook/%Y/%m/%d/', verbose_name='Le notebook')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Description')),
                ('slug', models.SlugField(blank=True, max_length=80, null=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1)),
                ('edited', models.BooleanField(default=False)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dev', to='users.user')),
            ],
            options={
                'verbose_name': 'Notebook',
                'verbose_name_plural': 'Notebooks',
                'ordering': ('-timestamp',),
            },
        ),
    ]

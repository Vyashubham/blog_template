# Generated by Django 2.2.12 on 2021-02-06 18:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=tinymce.models.HTMLField(),
        ),
    ]
# Generated by Django 2.2.12 on 2021-02-06 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Slug_Field',
            new_name='slug',
        ),
    ]
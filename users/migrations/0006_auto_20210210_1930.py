# Generated by Django 2.2.12 on 2021-02-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_vyasprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vyasprofile',
            name='Date_ended',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='vyasprofile',
            name='Date_started',
            field=models.DateField(),
        ),
    ]

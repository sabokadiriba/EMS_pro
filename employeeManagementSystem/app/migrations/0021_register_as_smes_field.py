# Generated by Django 4.1 on 2022-09-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_delete_fieldofstudies'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_as_smes',
            name='field',
            field=models.TextField(null=True),
        ),
    ]

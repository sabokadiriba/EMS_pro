# Generated by Django 4.1 on 2022-09-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_attendance_department_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_as_smes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campany', models.CharField(max_length=100)),
                ('campany_type', models.CharField(max_length=100)),
                ('field', models.TextField()),
                ('proposal', models.FileField(upload_to='file')),
            ],
        ),
    ]

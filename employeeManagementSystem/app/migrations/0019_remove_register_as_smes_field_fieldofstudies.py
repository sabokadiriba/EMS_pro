# Generated by Django 4.1 on 2022-09-03 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_register_as_smes_proposal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_as_smes',
            name='field',
        ),
        migrations.CreateModel(
            name='FieldOfStudies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('applayer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register_as_smes')),
            ],
        ),
    ]
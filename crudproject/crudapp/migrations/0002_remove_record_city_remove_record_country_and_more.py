# Generated by Django 5.1 on 2024-11-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='city',
        ),
        migrations.RemoveField(
            model_name='record',
            name='country',
        ),
        migrations.RemoveField(
            model_name='record',
            name='county',
        ),
        migrations.AddField(
            model_name='record',
            name='agent_name',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='record',
            name='agent_number',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='record',
            name='car_color',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='record',
            name='car_model',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='record',
            name='company_branch',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='record',
            name='plate_number',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
# Generated by Django 5.2 on 2025-04-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_title_data_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]

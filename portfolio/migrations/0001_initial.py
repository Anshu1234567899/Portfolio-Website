# Generated by Django 5.2.2 on 2025-06-17 13:09

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_title', models.CharField(max_length=100)),
                ('portfolio_desc', tinymce.models.HTMLField()),
            ],
        ),
    ]


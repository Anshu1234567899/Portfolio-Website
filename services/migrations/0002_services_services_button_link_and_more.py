# Generated by Django 5.2.2 on 2025-06-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='services_button_link',
            field=models.URLField(max_length=200),
        ),
        migrations.AddField(
            model_name='services',
            name='services_button_text',
            field=models.CharField(max_length=50),
        ),
    ]

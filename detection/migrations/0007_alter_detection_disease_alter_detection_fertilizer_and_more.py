# Generated by Django 4.2.7 on 2025-04-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0006_remove_blogpost_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='disease',
            field=models.TextField(default='Disease analysis pending'),
        ),
        migrations.AlterField(
            model_name='detection',
            name='fertilizer',
            field=models.TextField(default='Balanced NPK fertilizer'),
        ),
        migrations.AlterField(
            model_name='detection',
            name='water',
            field=models.TextField(default='Regular watering'),
        ),
    ]

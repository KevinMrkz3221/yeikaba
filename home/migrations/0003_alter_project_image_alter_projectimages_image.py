# Generated by Django 5.0.1 on 2024-01-21 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project_image_projectimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/projects/'),
        ),
        migrations.AlterField(
            model_name='projectimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/projects/'),
        ),
    ]

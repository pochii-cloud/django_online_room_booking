# Generated by Django 3.2.7 on 2021-11-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_rooms_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/rooms'),
        ),
    ]

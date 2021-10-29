# Generated by Django 3.2.7 on 2021-10-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('booked', models.BooleanField(default=False)),
                ('capacity', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
    ]
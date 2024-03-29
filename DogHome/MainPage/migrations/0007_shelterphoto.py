# Generated by Django 5.0 on 2023-12-22 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0006_delete_dogphotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShelterPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos/shelter/%Y/%m/%d/', verbose_name='Фото')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='MainPage.shelter')),
            ],
        ),
    ]

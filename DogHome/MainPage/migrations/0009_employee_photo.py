# Generated by Django 5.0 on 2024-02-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0008_employee_shelter'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/employee/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]

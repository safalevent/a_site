# Generated by Django 2.2.9 on 2020-01-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ogrenci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='Dogum_Tarihi',
            field=models.DateField(),
        ),
    ]

# Generated by Django 2.2.9 on 2020-01-01 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ogrenci', '0003_auto_20200101_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogrenci',
            old_name='İsim',
            new_name='Isim',
        ),
    ]

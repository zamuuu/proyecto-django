# Generated by Django 4.0.3 on 2022-03-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0002_alter_futbolista_club_futbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futbolista',
            name='club_futbol',
            field=models.CharField(max_length=50),
        ),
    ]

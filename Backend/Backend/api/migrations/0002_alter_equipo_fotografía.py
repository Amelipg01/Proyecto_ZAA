# Generated by Django 5.0.2 on 2024-04-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fotografía',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destino',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]

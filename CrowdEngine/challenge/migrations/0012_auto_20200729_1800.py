# Generated by Django 2.2 on 2020-07-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0011_auto_20200729_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='prize',
            field=models.IntegerField(default=1000),
        ),
    ]

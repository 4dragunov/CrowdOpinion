# Generated by Django 2.2 on 2020-08-19 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0021_auto_20200814_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_dislike',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_like',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]

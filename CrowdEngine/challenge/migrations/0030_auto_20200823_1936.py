# Generated by Django 2.2 on 2020-08-23 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0029_auto_20200823_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answerlike',
            old_name='answer_pk',
            new_name='answer',
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]

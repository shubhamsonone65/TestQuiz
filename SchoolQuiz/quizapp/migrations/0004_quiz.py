# Generated by Django 3.1.7 on 2021-04-21 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.TextField()),
                ('time', models.TimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.student')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.CharField(max_length=20)),
                ('courseTitle', models.CharField(max_length=50)),
                ('courseDays', models.CharField(max_length=10)),
                ('courseTime', models.CharField(max_length=30)),
                ('courseDiscipline_01', models.CharField(max_length=40)),
                ('courseDiscipline_02', models.CharField(max_length=40)),
                ('courseDiscipline_03', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=20)),
                ('maxLoad', models.IntegerField()),
                ('instructorDiscipline_01', models.CharField(max_length=40)),
                ('instructorDiscipline_02', models.CharField(max_length=40)),
                ('instructorDiscipline_03', models.CharField(max_length=40)),
            ],
        ),
    ]

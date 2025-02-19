# Generated by Django 5.0 on 2024-10-25 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=500)),
                ('grade', models.IntegerField(default=0.0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='CohortGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_join', models.DateTimeField(auto_now_add=True)),
                ('students', models.ManyToManyField(to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=300)),
                ('rating', models.FloatField(default=0.0)),
                ('profile_picture', models.ImageField(upload_to='student_profile')),
                ('date_join', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]

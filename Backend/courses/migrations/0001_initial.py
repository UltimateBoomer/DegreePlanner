# Generated by Django 5.1.2 on 2025-01-05 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('year', models.IntegerField()),
                ('season', models.CharField(choices=[('F', 'Fall'), ('W', 'Winter'), ('S', 'Spring')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CoReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coreqOrGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='AntiReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antireq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='PreReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created', to='courses.course')),
                ('prereqOrGroup', models.ManyToManyField(to='courses.course')),
            ],
        ),
    ]

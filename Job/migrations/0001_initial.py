# Generated by Django 5.0.1 on 2024-05-08 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('requirements', models.TextField()),
                ('responsibilities', models.TextField()),
                ('qualifications', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.job')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.recruiter'),
        ),
    ]

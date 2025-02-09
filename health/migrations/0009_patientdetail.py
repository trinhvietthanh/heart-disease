# Generated by Django 5.1.5 on 2025-02-03 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0008_auto_20210821_0121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chest_pain', models.CharField(max_length=100, null=True)),
                ('trestbps', models.CharField(max_length=100, null=True)),
                ('chol', models.CharField(max_length=100, null=True)),
                ('fbs', models.CharField(max_length=100, null=True)),
                ('restecg', models.CharField(max_length=100, null=True)),
                ('thalach', models.CharField(max_length=100, null=True)),
                ('exang', models.CharField(max_length=100, null=True)),
                ('oldpeak', models.CharField(max_length=100, null=True)),
                ('slope', models.CharField(max_length=100, null=True)),
                ('ca', models.CharField(max_length=100, null=True)),
                ('thal', models.CharField(max_length=100, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

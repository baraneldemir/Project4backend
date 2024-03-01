# Generated by Django 4.2.10 on 2024-02-29 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('twitter', models.TextField(max_length=250)),
                ('linkedin', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.people')),
            ],
        ),
    ]
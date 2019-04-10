# Generated by Django 2.1.7 on 2019-04-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=256, unique=True)),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2020-01-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='createresume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('objective', models.TextField()),
                ('experiance', models.IntegerField()),
                ('organization', models.CharField(max_length=100)),
                ('skills', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('EmailID', models.EmailField(max_length=254)),
                ('MobileNumber', models.BigIntegerField()),
                ('CheckIn', models.DateField()),
                ('CheckOut', models.DateField()),
            ],
        ),
    ]

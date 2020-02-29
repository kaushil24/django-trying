# Generated by Django 3.0.3 on 2020-02-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guests', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=64)),
                ('Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodBills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_Guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guests.Guest')),
            ],
        ),
    ]

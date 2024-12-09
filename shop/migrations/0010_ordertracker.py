# Generated by Django 3.1 on 2020-08-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200819_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTracker',
            fields=[
                ('tracker_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=20)),
                ('update_description', models.CharField(max_length=500)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
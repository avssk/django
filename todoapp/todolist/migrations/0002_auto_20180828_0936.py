# Generated by Django 2.0.7 on 2018-08-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

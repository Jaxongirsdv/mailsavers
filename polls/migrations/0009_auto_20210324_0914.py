# Generated by Django 3.1.7 on 2021-03-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210321_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='id',
        ),
        migrations.AlterField(
            model_name='mail',
            name='nomer',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Исходяший номер'),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210320_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='executor',
            field=models.CharField(max_length=50, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='sent_to',
            field=models.CharField(max_length=50, verbose_name='Кому'),
        ),
    ]

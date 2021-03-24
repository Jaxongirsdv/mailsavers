# Generated by Django 3.1.7 on 2021-03-20 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='mail',
            name='e_mail',
        ),
        migrations.AlterField(
            model_name='mail',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.staff', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='sent_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.org', verbose_name='Kove'),
        ),
    ]

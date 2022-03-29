# Generated by Django 3.2.8 on 2022-03-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20220328_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teachers', to='school.Teacher', verbose_name='Учитель'),
        ),
    ]
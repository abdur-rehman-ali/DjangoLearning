# Generated by Django 4.2.5 on 2023-09-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('1st', 'First'), ('2nd', 'Second'), ('3rd', 'Third'), ('4th', 'Fourth')], default='1st', max_length=4),
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-19 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_time_dayoftheweeks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedulestudentprofessor',
            options={'managed': True, 'verbose_name': 'ScheduleStudentProfessor', 'verbose_name_plural': 'ScheduleStudentProfessors'},
        ),
        migrations.AlterModelTable(
            name='schedulestudentprofessor',
            table='',
        ),
    ]

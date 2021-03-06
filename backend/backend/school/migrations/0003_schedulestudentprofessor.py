# Generated by Django 2.2.6 on 2019-11-18 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleStudentProfessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Professor')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Schedule')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbrc', '0009_alter_student_m3_alter_student_sgpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attende',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RedgNo', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]

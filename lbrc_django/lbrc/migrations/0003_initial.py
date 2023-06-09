# Generated by Django 4.0.4 on 2022-05-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lbrc', '0002_delete_attende'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_NO', models.IntegerField()),
                ('RedgNo', models.CharField(max_length=10)),
                ('M3', models.CharField(max_length=5)),
                ('DMS', models.CharField(max_length=5)),
                ('DBMS', models.CharField(max_length=5)),
                ('CO', models.CharField(max_length=5)),
                ('OOP', models.CharField(max_length=5)),
                ('DBMSLAB', models.CharField(max_length=5)),
                ('RLAB', models.CharField(max_length=5)),
                ('WADFSLAB', models.CharField(max_length=5)),
                ('SGPA', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

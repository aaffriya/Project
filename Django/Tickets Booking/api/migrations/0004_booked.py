# Generated by Django 4.0.2 on 2022-03-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie', models.CharField(max_length=100)),
                ('Theater', models.CharField(max_length=100)),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]

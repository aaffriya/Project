# Generated by Django 4.0.2 on 2022-03-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_booked_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='Time',
            field=models.DateField(null=True),
        ),
    ]

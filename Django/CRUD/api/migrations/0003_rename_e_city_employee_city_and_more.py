# Generated by Django 4.0.2 on 2022-02-27 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_person_employee_delete_employeee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='E_city',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='E_Email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='E_mobile',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='E_name',
            new_name='Name',
        ),
    ]
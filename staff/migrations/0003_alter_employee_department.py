# Generated by Django 4.1 on 2022-08-12 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_employee_contact_alter_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='staff.department'),
        ),
    ]

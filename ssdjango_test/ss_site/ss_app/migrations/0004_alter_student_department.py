# Generated by Django 4.2.7 on 2023-12-14 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ss_app', '0003_department_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ss_app.department'),
        ),
    ]

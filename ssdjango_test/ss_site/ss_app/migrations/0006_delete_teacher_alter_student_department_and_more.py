# Generated by Django 4.2.7 on 2023-12-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss_app', '0005_alter_department_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]

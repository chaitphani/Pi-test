# Generated by Django 3.2.6 on 2021-08-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piapp', '0005_alter_kpimodel_work_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpimodel',
            name='current_status',
            field=models.CharField(max_length=50),
        ),
    ]

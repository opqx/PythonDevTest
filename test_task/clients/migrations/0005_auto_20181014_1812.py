# Generated by Django 2.1.1 on 2018-10-14 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20181014_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Companies'),
        ),
    ]
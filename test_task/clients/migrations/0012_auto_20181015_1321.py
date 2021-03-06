# Generated by Django 2.1.1 on 2018-10-15 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_auto_20181015_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Companies'),
        ),
        migrations.AlterField(
            model_name='building',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Street'),
        ),
        migrations.AlterField(
            model_name='city',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Companies'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Region'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Companies'),
        ),
        migrations.AlterField(
            model_name='office',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Building'),
        ),
        migrations.AlterField(
            model_name='office',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Companies'),
        ),
        migrations.AlterField(
            model_name='region',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Companies'),
        ),
        migrations.AlterField(
            model_name='region',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Country'),
        ),
    ]

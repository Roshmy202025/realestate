# Generated by Django 5.0.1 on 2024-01-08 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_management', '0005_tenant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_end_date', models.DateField()),
                ('monthly_rent_date', models.PositiveSmallIntegerField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_management.tenant')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_management.unit')),
            ],
        ),
    ]

# Generated by Django 5.2.3 on 2025-06-29 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('prodct_type', models.CharField(choices=[('TECH', 'Laptop'), ('EDU', 'Book'), ('SPT', 'Stamp'), ('FMCG', 'Kurkure'), ('SD', 'Cocacola')], max_length=4)),
            ],
        ),
    ]

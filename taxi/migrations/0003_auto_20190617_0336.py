# Generated by Django 2.1.7 on 2019-06-17 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_auto_20190617_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxi.Client'),
        ),
    ]

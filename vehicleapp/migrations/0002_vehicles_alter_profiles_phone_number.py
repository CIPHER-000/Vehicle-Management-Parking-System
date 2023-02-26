# Generated by Django 4.1.7 on 2023-02-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=200)),
                ('plate_number', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('is_active', models.BooleanField()),
                ('entry_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('exit_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='profiles',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
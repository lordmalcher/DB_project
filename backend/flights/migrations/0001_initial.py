# Generated by Django 2.2.7 on 2019-11-11 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(max_length=2)),
                ('icao_code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produced', models.DateField()),
                ('registration', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AirplaneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IATA_code', models.CharField(max_length=3, unique=True)),
                ('ICAO_code', models.CharField(max_length=4, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('continent', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=50)),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Airline')),
                ('airplane', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flights.Airplane')),
                ('crew', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flights.Crew')),
                ('from_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from+', to='flights.Airport')),
                ('to_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to+', to='flights.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Luggage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('weight_limit', models.IntegerField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Reservation')),
            ],
        ),
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('airline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flights.Airline')),
                ('crew', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flights.Crew')),
            ],
        ),
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flights.Country'),
        ),
        migrations.AddField(
            model_name='airplane',
            name='airplane_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.AirplaneModel'),
        ),
        migrations.AddField(
            model_name='airline',
            name='base_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flights.Airport'),
        ),
    ]

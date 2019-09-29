# Generated by Django 2.2.4 on 2019-09-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('houses', '0012_invitation'),
	]

	operations = [
		migrations.AddField(
			model_name='house',
			name='cats_allowed',
			field=models.BooleanField(default=False),
		),
		migrations.AddField(
			model_name='house',
			name='dogs_allowed',
			field=models.BooleanField(default=False),
		),
		migrations.AddField(
			model_name='house',
			name='has_dishwasher',
			field=models.BooleanField(default=False),
		),
		migrations.AddField(
			model_name='house',
			name='has_laundry',
			field=models.BooleanField(default=False),
		),
		migrations.AddField(
			model_name='house',
			name='num_bathrooms',
			field=models.IntegerField(default=-1),
		),
		migrations.AddField(
			model_name='house',
			name='num_female',
			field=models.IntegerField(default=-1),
		),
		migrations.AddField(
			model_name='house',
			name='num_male',
			field=models.IntegerField(default=-1),
		),
		migrations.AddField(
			model_name='house',
			name='num_parking_spaces',
			field=models.IntegerField(default=-1),
		),
		migrations.AddField(
			model_name='house',
			name='num_rooms',
			field=models.IntegerField(default=-1),
		),
		migrations.AddField(
			model_name='house',
			name='pets_allowed',
			field=models.BooleanField(default=False),
		),
	]

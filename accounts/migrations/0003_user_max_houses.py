# Generated by Django 2.2.4 on 2019-09-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('accounts', '0002_auto_20190828_1535'),
	]

	operations = [
		migrations.AddField(
			model_name='user',
			name='max_houses',
			field=models.IntegerField(default=1),
		),
	]

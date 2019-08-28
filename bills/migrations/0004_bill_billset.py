# Generated by Django 2.2.4 on 2019-08-28 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0012_invitation'),
        ('bills', '0003_auto_20190828_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(auto_now=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ElEC', 'Electricity'), ('WATER', 'Water'), ('GAS', 'Gas'), ('INTER', 'Internet'), ('OTHER', 'Other')], max_length=5)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now=True)),
                ('file', models.FileField(default=None, upload_to='')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.BillSet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
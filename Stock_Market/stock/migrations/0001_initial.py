# Generated by Django 3.2.3 on 2021-08-15 16:16

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
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=255)),
                ('catagory', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('rate', models.FloatField(max_length=100)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
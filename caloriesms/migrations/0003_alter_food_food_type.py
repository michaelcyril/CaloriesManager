# Generated by Django 3.2.19 on 2023-05-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caloriesms', '0002_auto_20230513_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_type',
            field=models.CharField(max_length=200),
        ),
    ]
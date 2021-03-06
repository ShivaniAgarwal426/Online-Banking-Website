import bank.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acct_no',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, validators=[bank.models.len11]),
        ),
        migrations.AlterField(
            model_name='account',
            name='pin',
            field=models.PositiveSmallIntegerField(validators=[bank.models.len6]),
        ),
        migrations.AlterField(
            model_name='cust_phone',
            name='phno',
            field=models.CharField(max_length=10, validators=[bank.models.len10]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pan',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[bank.models.validate_pan]),
        ),
    ]

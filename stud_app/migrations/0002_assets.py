# Generated by Django 2.1.5 on 2019-02-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=200)),
                ('asset_dep', models.CharField(choices=[('sports', 'SPORTS'), ('library', 'LIBRARY'), ('uniform', 'UNIFORM')], default='sports', max_length=30)),
                ('vendor_name', models.CharField(max_length=30)),
                ('receiver_name', models.CharField(max_length=30)),
                ('class_name', models.CharField(choices=[('lkg', 'LKG'), ('ukg', 'UKG'), ('I Standard', 'I STANDARD'), ('II Standard', 'II STANDARD'), ('III Standard', 'III STANDARD'), ('IV Standard', 'IV STANDARD'), ('V Standard', 'V STANDARD'), ('VI Standard', 'VI STANDARD'), ('VII Standard', 'VII STANDARD'), ('VIII Standard', 'VIII STANDARD'), ('IX Standard', 'IX STANDARD'), ('X Standard', 'X STANDARD')], default='lkg', max_length=30)),
                ('asset_type', models.CharField(choices=[('regular uniform', 'REGULAR UNIFORM'), ('sports uniform', 'SPORTS UNIFORM'), ('shoes', 'SHOES'), ('books', 'BOOKS')], default='regular uniform', max_length=30)),
                ('purchase_date', models.DateField(null=True)),
                ('amount', models.CharField(max_length=30)),
                ('pay_status', models.CharField(choices=[('in Stock', 'in Stock'), ('Out of stock', 'Out of stock'), ('issue', 'ISSUE')], default='in Stock', max_length=40)),
                ('ref_number', models.CharField(max_length=50)),
                ('asset_details', models.CharField(max_length=400)),
            ],
        ),
    ]

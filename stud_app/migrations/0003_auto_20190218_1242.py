# Generated by Django 2.1.5 on 2019-02-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0002_assets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='asset_dep',
            field=models.CharField(choices=[('Sports', 'SPORTS'), ('Library', 'LIBRARY'), ('Uniforms', 'UNIFORM')], max_length=30),
        ),
        migrations.AlterField(
            model_name='assets',
            name='asset_type',
            field=models.CharField(choices=[('Regular Uniforms', 'REGULAR UNIFORM'), ('Sports Uniforms', 'SPORTS UNIFORM'), ('Shoes', 'SHOES'), ('Books', 'BOOKS')], max_length=30),
        ),
        migrations.AlterField(
            model_name='assets',
            name='class_name',
            field=models.CharField(choices=[('lkg', 'LKG'), ('ukg', 'UKG'), ('I Standard', 'I STANDARD'), ('II Standard', 'II STANDARD'), ('III Standard', 'III STANDARD'), ('IV Standard', 'IV STANDARD'), ('V Standard', 'V STANDARD'), ('VI Standard', 'VI STANDARD'), ('VII Standard', 'VII STANDARD'), ('VIII Standard', 'VIII STANDARD'), ('IX Standard', 'IX STANDARD'), ('X Standard', 'X STANDARD')], max_length=30),
        ),
        migrations.AlterField(
            model_name='assets',
            name='pay_status',
            field=models.CharField(choices=[('In Stock', 'in Stock'), ('Out Of Stock', 'Out of stock'), ('Issue', 'ISSUE')], max_length=40),
        ),
    ]

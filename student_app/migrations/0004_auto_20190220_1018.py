# Generated by Django 2.1.5 on 2019-02-20 10:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_auto_20190220_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mob_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='parents_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='sib_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Sibling Contact phone number', max_length=128),
        ),
    ]

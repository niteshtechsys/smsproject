# Generated by Django 2.1.5 on 2019-02-20 11:10

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_auto_20190220_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mob_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='student',
            name='parents_phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='student',
            name='sib_phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
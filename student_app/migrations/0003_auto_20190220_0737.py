# Generated by Django 2.1.5 on 2019-02-20 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20190220_0612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gender',
            new_name='pay_choice',
        ),
    ]

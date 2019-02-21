from django.db import models
from datetime import date
#from phonenumber_field.modelfields import PhoneNumberField

from phone_field import PhoneField


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_lastname = models.CharField(max_length=100)
    Registration_date = models.DateField(null=True,blank=False)
    class_name_choices=(
    ("lkg","LKG"),
    ("ukg","UKG"),
    ("I Standard","I STANDARD"),
    ("II Standard","II STANDARD"),
    ("III Standard","III STANDARD"),
    ("IV Standard","IV STANDARD"),
    ("V Standard","V STANDARD"),
    ("VI Standard","VI STANDARD"),
    ("VII Standard","VII STANDARD"),
    ("VIII Standard","VIII STANDARD"),
    ("IX Standard","IX STANDARD"),
    ("X Standard","X STANDARD"),
    )
    class_name = models.CharField(max_length=30 ,choices=class_name_choices)
    gender_choice=(
    ("Male","MALE"),
    ("Female","FEMALE"),
    )
    gender_type = models.CharField(max_length=30,choices=gender_choice)
    mob_number = PhoneField(blank=False,null=False,unique=False)
    parents_name = models.CharField(max_length=100)
    parents_phone = PhoneField(blank=False,null=False,unique=False)
    Birth_date = models.DateField(null=True,blank=False)
    Blood_group = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    rti = models.BooleanField(default=False)
    sibling = models.BooleanField(default=False)
    sib_class_name_choices=(
    ("lkg","LKG"),
    ("ukg","UKG"),
    ("I Standard","I STANDARD"),
    ("II Standard","II STANDARD"),
    ("III Standard","III STANDARD"),
    ("IV Standard","IV STANDARD"),
    ("V Standard","V STANDARD"),
    ("VI Standard","VI STANDARD"),
    ("VII Standard","VII STANDARD"),
    ("VIII Standard","VIII STANDARD"),
    ("IX Standard","IX STANDARD"),
    ("X Standard","X STANDARD"),
    )
    sib_class_name = models.CharField(max_length=30 ,choices=sib_class_name_choices)
    sib_rel_choices=(
    ("Brother","Brother"),
    ("Sister","Sister"),
    )
    sib_rel_name = models.CharField(max_length=30 ,choices=sib_rel_choices)
    sib_phone = PhoneField(blank=False,null=False,unique=False)
    sib_name = models.CharField(max_length=100)
    pay_choice = (
    ('monthly', 'monthly'),
    ('yearly', 'yearly'),
    ('session', 'session'),
    )
    pay_choice = models.CharField(choices=pay_choice,max_length=50)
    fees_amount = models.CharField(max_length=50)
    ref_number = models.CharField(max_length=50)
    pay_type_choices=(
    ("Cash","Cash"),
    ("Cheque","Cheque"),
    ("Online Transfer","Online Transfer"),
    ("Draft","Draft"),
    ("Other","Other"),
    )
    pay_type = models.CharField(max_length=30 ,choices=pay_type_choices)
    pay_status_choice=(
    ("Paid","Paid"),
    ("Unpaid","Unpaid"),
    ("Pending","Pending"),
    )
    pay_status = models.CharField(max_length=30 ,choices=pay_status_choice)
    pay_details = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name

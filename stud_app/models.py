from django.db import models
from datetime import date



# Create your models here.
class Holiday(models.Model):
    holiday_name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.holiday_name

class Assets(models.Model):
    asset_name = models.CharField(max_length=200)
    asset_dep_choices=(
    ("Sports","SPORTS"),
    ("Library","LIBRARY"),
    ("Uniforms","UNIFORM"),
    )
    asset_dep = models.CharField(max_length=30,choices=asset_dep_choices)
    vendor_name = models.CharField(max_length=30)
    receiver_name = models.CharField(max_length=30)

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
    asset_type_choices=(
    ("Regular Uniforms","REGULAR UNIFORM"),
    ("Sports Uniforms","SPORTS UNIFORM"),
    ("Shoes","SHOES"),
    ("Books","BOOKS"),

    )
    asset_type = models.CharField(max_length=30,choices=asset_type_choices)
    purchase_date = models.DateField(null=True,blank=False)
    amount = models.CharField(max_length=30)
    pay_status_choices=(
    ("In Stock","in Stock"),
    ("Out Of Stock","Out of stock"),
    ("Issue","ISSUE"),
    )
    pay_status = models.CharField(max_length=40 ,choices=pay_status_choices)
    ref_number = models.CharField(max_length=50)
    asset_details = models.CharField(max_length=200)

    def __str__(self):
        return self.asset_name

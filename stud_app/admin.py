from django.contrib import admin

# Register your models here.
from .models import Holiday
from .models import Assets

admin.site.register(Holiday)
admin.site.register(Assets)

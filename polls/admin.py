from django.contrib import admin

# Register your models here.
from .models import Mail,Org,Staff

admin.site.register(Mail)
admin.site.register(Org)
admin.site.register(Staff)
from django.contrib import admin

# Register your models here.
from .models import Testing,gateway_details,gateway
admin.site.register(Testing)
admin.site.register(gateway)
admin.site.register(gateway_details)
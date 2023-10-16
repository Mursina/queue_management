from django.contrib import admin
from . import models

# Register your models here.
class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'counter', 'service', 'created')

class CounterAdmin(admin.ModelAdmin):
    list_display = ('counter_id', 'service_id', 'status')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'service_name')

admin.site.register(models.Counter, CounterAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Token, TokenAdmin)
from django.db import models

# Create your models here.

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    counter = models.ForeignKey('Counter', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)


class Counter(models.Model):
    counter_id = models.AutoField(primary_key=True)
    service_id = models.ForeignKey('Service', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)


class System(models.Model):
    number_of_counters = models.PositiveIntegerField()
    services = models.JSONField()
    service_per_counter = models.JSONField()
    counter_status = models.JSONField()
    token_limit_per_counter = models.PositiveBigIntegerField()
    service_modes = models.JSONField()
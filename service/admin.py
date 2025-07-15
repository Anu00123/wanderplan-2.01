from django.contrib import admin
from .models import InsurancePlan,InsurancePayment
# Register your models here.
admin.site.register(InsurancePlan)
admin.site.register(InsurancePayment)
from django.contrib import admin

# Register your models here.
from .models import Package,PackageImage,ContactSubmission,Booking

admin.site.register(Package)
admin.site.register(PackageImage)
admin.site.register(ContactSubmission)
admin.site.register(Booking)
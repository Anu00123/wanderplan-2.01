# models.py
from django.db import models
from django.utils import timezone
import uuid
from datetime import timedelta

class InsurancePlan(models.Model):
    PLAN_TYPES = [
        ('BASIC', 'Basic'),
        ('STANDARD', 'Standard'),
        ('PREMIUM', 'Premium'),
    ]
    
    plan_type = models.CharField(max_length=10, choices=PLAN_TYPES, unique=True)
    daily_price = models.DecimalField(max_digits=6, decimal_places=2)
    emergency_medical = models.DecimalField(max_digits=10, decimal_places=2)
    trip_cancellation = models.DecimalField(max_digits=10, decimal_places=2)
    baggage_loss = models.DecimalField(max_digits=10, decimal_places=2)
    adventure_sports = models.BooleanField(default=False)
    rental_car_coverage = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_plan_type_display()



class InsurancePayment(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    aadhar_number = models.CharField(max_length=12)
    trip_name = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=20, unique=True)
    
    

    def save(self, *args, **kwargs):
        if not self.policy_number:
            # Generate policy number: WP + current year + random 6 digits
            self.policy_number = f"WP{timezone.now().year}-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)
    
    @property
    def expiry_date(self):
        return self.payment_time + timedelta(days=365)
    
    def __str__(self):
        return f"{self.transaction_id} - {self.plan_name}"



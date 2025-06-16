from django.db import models
from django.urls import reverse
from django.utils import timezone



class Package(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.TextField()
    location = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    main_image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    duration_days = models.PositiveIntegerField()
    duration_nights = models.PositiveIntegerField()
    

    includes = models.TextField(blank=True, help_text="What's included in the package")
    excludes = models.TextField(blank=True, help_text="What's not included")

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('package_detail', kwargs={'pk': self.pk})
    
    def get_rating_stars(self):
        full_stars = int(self.rating)
        half_star = self.rating - full_stars >= 0.5
        empty_stars = 5 - full_stars - (1 if half_star else 0)
        return {
            'full_stars': range(full_stars),
            'half_star': half_star,
            'empty_stars': range(empty_stars)
        }

class PackageImage(models.Model):
    package = models.ForeignKey(Package, related_name='images', on_delete=models.CASCADE)
    image = models.URLField()
    caption = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.package.title}"
    

class ContactSubmission(models.Model):
    SUBJECT_CHOICES = [
        ('package', 'Package Inquiry'),
        ('booking', 'Booking Assistance'),
        ('custom', 'Custom Trip Request'),
        ('general', 'General Question'),
    ]
    
    fullName  = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Contact from {self.fullName} - {self.subject}"
    
    class Meta:
        ordering = ['-submitted_at']




from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone



class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Booking for {self.package.title} by {self.name}"
    
    class Meta:
        ordering = ['-created_at']
from django.db import models

class Listing(models.Model):
    PROPERTY_TYPES = [
        ('ev', 'Ev'),
        ('arsa', 'Arsa'),
        ('tarla', 'Tarla'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

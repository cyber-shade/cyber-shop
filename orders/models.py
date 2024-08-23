from django.db import models

# Create your models here.
class Invoice(models.Model):
    CANCELED = 0 
    PENDING = 1
    REGISTERED = 2
    CONFIRMED = 3
    DELIVERED = 4 
    CLOSED = 5
    RETURNED = 6

    STATUS_CHOICES = (
        (CANCELED, 'canceled'),
        (PENDING, 'pending'),
        (REGISTERED, 'registered'),
        (CONFIRMED, 'confirmed'),
        (DELIVERED, 'delivered'),
        (CLOSED, 'closed'),
        (RETURNED, 'returned'),
    )

    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField('products.Product', related_name='invoices')
    sending_address = models.TextField()
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)
    payment_code = models.IntegerField()
    registration_date = models.DateTimeField(auto_now_add=True)
    sending_date = models.DateTimeField()


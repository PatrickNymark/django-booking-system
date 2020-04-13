from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    premium = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)


class Freelancer(models.Model, ):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

class Task(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    expected_hours = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    hour_price = models.IntegerField(default=0)
    description = models.TextField(default="")
    have_materials = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        self.total_price = self.hour_price * self.expected_hours
        super(Task, self).save(*args, **kwargs)


   



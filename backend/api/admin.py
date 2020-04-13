from django.contrib import admin
from .models import Task, Freelancer, Customer
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    fields = ['title', 'customer', 'freelancer', 'category', 'address', 'expected_hours', 'hour_price', 'description', 'have_materials', 'is_urgent']

class FreelancerAdmin(admin.ModelAdmin):
    fields = ['verified', 'user']

class CustomerAdmin(admin.ModelAdmin):
    fields = ['premium', 'user']

admin.site.register(Task, TaskAdmin)
admin.site.register(Freelancer, FreelancerAdmin)
admin.site.register(Customer, CustomerAdmin)

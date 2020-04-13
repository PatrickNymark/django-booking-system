from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Customer, Task, Freelancer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'user_permissions']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['is_online', 'premium', 'user']

        
class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = ['is_online', 'verified', 'user']
        

class TaskSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.id')
    
    class Meta:
        model = Task
        fields = '__all__'


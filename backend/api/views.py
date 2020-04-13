from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import TaskForm, CreateUserForm, SearchForm, FilterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Q
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, CustomerSerializer, TaskSerializer, FreelancerSerializer
from django.contrib.auth.models import User, Group
from .models import Customer, Freelancer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
def home(request):
    context = {
        'tasks': Task.objects.all(),
        'title': 'Home'
    }

    return render(request, 'home.html', context)

def schedule(request):
    return render(request, 'schedule.html')

def tasks(request):
    search_form = SearchForm()
    filter_form = FilterForm()

    max_price = Task.objects.aggregate(Max('total_price'))
    min_price = Task.objects.aggregate(Min('total_price'))
    print(request.POST.get('price_range'))

    context = {}
    if request.method == 'POST':
        # if request.POST.get('search_value'):
        #     search_form = SearchForm(request.POST)
        #     tasks = Task.objects.filter(title__contains=search_form.data['search_value']).order_by('-date')

        #     context['tasks'] = tasks
        #     context['search_form'] = search_form
        #     context['total_tasks'] = len(tasks)
           
            
        #     return render(request, 'tasks.html', context)

        filter_form = FilterForm(request.POST)
        current_max_price = 0
        current_min_price = 0
        tasks = Task.objects.all()

        categories = []

        if request.POST.get('price_range'):
            price_range = filter_form.data['price_range']
            current_max_price = price_range.split(' ')[3]
            current_min_price = price_range.split(' ')[0]
            tasks = tasks.filter(total_price__gte=current_min_price , total_price__lte=current_max_price)
        else:
            print(max_price)
            current_max_price = max_price['total_price__max']
            current_min_price = min_price['total_price__min']
        

        ## refactor....
        if request.POST.get('painting'):
            categories.append('Painting')
        
        if request.POST.get('plumbing'):
            categories.append('Plumbing')
        
        if request.POST.get('carpentry'):
            categories.append('Carpentry')
    
        if request.POST.get('cleaning'):
            categories.append('Cleaning')

        if len(categories) == 1:
            tasks = tasks.filter(category__icontains=categories[0])
        elif len(categories) == 2:
            tasks = tasks.filter( Q(category__contains=categories[0]) | Q(category__contains=categories[1]))
        elif len(categories) == 3:
            tasks = tasks.filter( Q(category__contains=categories[0]) | Q(category__contains=categories[1]) | Q(category__contains=categories[2]))
        elif len(categories) == 4:
            tasks = tasks.filter( Q(category__contains=categories[0]) | Q(category__contains=categories[1]) | Q(category__contains=categories[2]) | Q(category__contains=categories[3]))
        else:
            pass
        ## ...

        is_urgent = False
        if request.POST.get('is_urgent'):
            is_urgent = True
            tasks = tasks.filter(is_urgent=True)

        ## Check search value
        if request.POST.get('search_value'):
            search_form = SearchForm(request.POST)
            tasks = tasks.filter(title__contains=search_form.data['search_value'])

            # context['tasks'] = tasks
            # context['search_form'] = search_form
            # context['total_tasks'] = len(tasks)
       
        # tasks = tasks.filter(total_price__gte=current_min_price , total_price__lte=current_max_price).order_by('-date')
        context['tasks'] = tasks.order_by('-date')
        context['search_form'] = search_form
        context['current_categories'] = categories
        context['filter_form'] = filter_form
        context['current_price_range'] =[{'total_price__max': current_max_price}, {'total_price__min': current_min_price}]
        context['total_tasks'] = len(tasks)
        context['price_range'] = [max_price, min_price]
        context['current_is_urgent'] = is_urgent

        return render(request, 'tasks.html', context)



    context['tasks'] = Task.objects.all().order_by('-date')
    context['search_form'] = search_form
    context['total_tasks'] = len(context['tasks'])
    context['price_range'] = [max_price, min_price]
    context['current_price_range'] = [max_price, min_price]
    return render(request, 'tasks.html', context)

@login_required(login_url='schedule-login')
def profile(request):
    user = request.user
    print(user)
    context = {
        'user': user
    }
    return render (request, "profile.html",context)

def register(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # message.success(request, f'Account was created for: {user}')

            return redirect('login')

    context = { 'form': form }
    return render(request, 'register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')


@login_required(login_url="schedule-login")
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API read-only endpoints to all/single task instances. 
    Permissions allowed to staff/superuser status.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint represent all customer instances, and create new customer instance.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permissions_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoints to present all tasks, and crud operations on single instances.
    Read permission to all authenticated users, and write permission if customer owns task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @action(detail=False)
    def by_title(self, request):
        tasks = Task.objects.filter(title__contains=request.query_params.get('title'))
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    

class FreelancerViewSet(viewsets.ModelViewSet):
    """
    API endpoints to present all freelancers, and crud operations on single instances.
    """
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer
    permission_classes = [IsAuthenticated]

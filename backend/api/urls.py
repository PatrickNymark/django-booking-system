"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'freelancers', views.FreelancerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', views.home, name="schedule-home"),
    path('planner/', views.schedule, name="schedule-planner"),
    path('register/', views.register, name="schedule-register"),
    path('login/', views.loginPage, name="schedule-login"),
    path('logout/', views.logoutUser, name="schedule-logout"),
    path('dashboard/', views.dashboard, name="schedule-dashboard"),
    path('view/tasks/', views.tasks, name="schedule-tasks"),
    path('profile/', views.profile, name="schedule-profile"),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TaskListAPIView, CreateUserAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('users/', CreateUserAPIView.as_view(), name='create-user'),
]
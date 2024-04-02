from django.urls import path, include
from auth_app import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user-registration', views.UserRegistrationViewSet,
                basename='user-registration')
router.register('user-login', views.UserLoginViewSet, basename='user-login')
router.register('user-logout', views.UserLogoutViewSet, basename='user-logout')
router.register('csrf-token', views.CSRFTokenViewSet, basename='csrf-token')

urlpatterns = [
    path('', include(router.urls))
]

from django.urls import path, include
from movie_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movie', views.MovieViewSet, basename='movie')
router.register('rating', views.RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]

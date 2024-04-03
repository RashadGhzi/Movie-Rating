from movie_app.models import Movie, Rating
from movie_app.serializers import MovieSerializer, RatingSerializer
from auth_app.views import BaseCommonViewSet

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django.db.models import Avg
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class MovieViewSet(BaseCommonViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as validationError:
            return Response(validationError.detail, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        snippets = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        movie = self.get_object()
        movie_average_rating = Rating.objects.filter(
            movie_id=movie).aggregate(Avg('rating'))['rating__avg']
        if movie_average_rating is None:
            movie_average_rating = 0.0
        data = {
            "movie_name": movie.name,
            "movie_average_rating": round(movie_average_rating, 1),
        }
        return Response(data, status=status.HTTP_200_OK)


@method_decorator(csrf_protect, name='dispatch')
class RatingViewSet(BaseCommonViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        request_data = request.data.copy()
        request_data['user_id'] = user.id
        serializer = self.get_serializer(data=request_data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as validationError:
            return Response(validationError.detail, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request, *args, **kwargs):
        ratings = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
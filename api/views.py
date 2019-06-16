from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(details=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            stars = request.data['stars']
            movie = Movie.objects.all(id=pk)
            user = User.objects.get(id=1)

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializers = RatingSerializer(rating, many=False)
                response = {'message':'Rating updated', 'result':serializers.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                Rating.objects.create(user=user.id, movie=movie.id, stars=stars)
                serializers = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializers.data}
                return Response(response, status=status.HTTP_200_OK)

            response = {'message', 'It\'s working!'}
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message', 'You need to provide stars.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

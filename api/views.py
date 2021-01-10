from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#ModelViewSet gives us some built in methods -- create, retrieve, update, partial update, destroy and list
#It is very helpful, but perhaps we want to create our own custom method?
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, ) #This lets django know to use our token that we pass in the request
    permission_classes = (IsAuthenticated, )
    @action(detail=True, methods=['POST']) #detail means we want to accept details (a specific Movie), not just "/"  
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data: #request data is the body of the request. 
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user #should be user that logged in; but need to set up login stuff for us to be able to grab it
            # user = User.objects.get(id=1)
            print('user', user)

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data} 
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data} 
                return Response(response, status=status.HTTP_200_OK)

            response = {'message': 'its working'} #starts won't be validated based on Model without link
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'} 
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'} 
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
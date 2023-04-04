from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status, viewsets

from .models import (
    Country,
    Producer,
    Car,
    Comment
)
from .serializers import (
    CountrySerializator,
    ProducerSerializtor,
    CarSerializator,
    CommentSerializator,
)


class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializator
    lookup_field = 'name'

    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class ProducerViewset(viewsets.ModelViewSet):
    queryset = Producer.objects.all().select_related('country')
    serializer_class = ProducerSerializtor
    lookup_field = 'name'

    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset_put(self, name):
        query = Producer.objects.get(name=name)

        if query:
            return query
        
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, name):
        instance = self.get_queryset_put(name)
        serializer = ProducerSerializtor(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CarViewset(viewsets.ModelViewSet):
    serializer_class = CarSerializator
    queryset = Car.objects.all().select_related('producer')
    lookup_field = 'name'
    raise_exception = True

    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def put(self, request, name):
        try:
            instance = Car.objects.get(name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CarSerializator(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializator
    queryset = Comment.objects.all().select_related('car')
    raise_exception = True

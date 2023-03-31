from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework import viewsets

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
    CommentSerializator
)


class CountryViewset(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializator
    lookup_field = 'name'

    # def get_queryset_destroy(self):
    #     query = Country.objects.get(name=self.request.data.get('name'))
        
    #     return query
    
    # def get_queryset_put(self):
    #     query = Country.objects.get(name=self.request.data.get('update_name', False))

    #     if query:
    #         return query
        
    #     return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    # def destroy(self, request, *args, **kwargs):
    #     country = self.get_queryset_destroy()
    #     serializator = CountrySerializator(country)

    #     if serializator.is_valid():
    #         self.perform_destroy(country) 
    #         serializator.save()  
    #         return Response(status=status.HTTP_204_NO_CONTENT) 
        
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request):
    #     query = self.get_queryset_put()
    #     serializer = CountrySerializator(instance=query, data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()

    #         return Response(status=status.HTTP_200_OK)
    #     else:    
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


class ProducerViewset(viewsets.ModelViewSet):

    queryset = Producer.objects.all().select_related('country')
    serializer_class = ProducerSerializtor
    lookup_field = 'name'

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
    queryset = Comment.objects.all()
    raise_exception = True

# class CountryListAPIView(APIView):

#     def get(self, request):
#         countries = Country.objects.all()
#         serializator = CountrySerializator(countries, many=True)

#         return Response(serializator.data)


# class CountryCreateAPIView(APIView):

#     def post(self, request):
#         serializator = CountrySerializator(data=request.data  )
        
#         if serializator.is_valid():
#             serializator.save()

#             return Response(serializator.data)
#         else:    
#             return Response(status=400)


# class CountryDeleteAPIView(DestroyAPIView):

#     serializer_class = CountrySerializator

#     def get_queryset(self):
#         query = Country.objects.get(name=self.request.data.get('name'))
        
#         return query
    
#     def destroy(self, request, *args, **kwargs):
#         country = self.get_queryset()
#         country.delete()
#         self.perform_destroy(country)

#         return Response(status=status.HTTP_200_OK)
    

# class CountryPutAPIView(APIView):

#     def get_queryset(self):
#         query = Country.objects.get(name=self.request.data.get('update_name', False))

#         if query:
#             return query
        
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def put(self, request):
#         query = self.get_queryset()
#         serializer = CountrySerializator(instance=query, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()

#             return Response(status=status.HTTP_200_OK)
#         else:    
#             return Response(status=400)

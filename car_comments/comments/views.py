from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Country
from .serializers import CountrySerializator


class CountryCreateAPIView(APIView):

    def post(self, request):
        serializator = CountrySerializator(data=request.data  )
        
        if serializator.is_valid():
            serializator.save()
            return Response(serializator.data)
        else:    
            return Response(status=400)
        

class CountryListAPIView(APIView):

    def get(self, request):
        countries = Country.objects.all()
        serializator = CountrySerializator(countries, many=True)

        return Response(serializator.data)


class CountryDeleteAPIView(DestroyAPIView):

    serializer_class = CountrySerializator

    def get_queryset(self):
        query = Country.objects.get(name=self.request.data.get('name'))
        
        return query
    
    def delete(self, request, *args, **kwargs):
        try:
            country = Country.objects.get(name=self.request.data.get('name'))
            country.delete()

            return Response({'status': 'success'})
        
        except:
            return Response({'status': 'failed'})

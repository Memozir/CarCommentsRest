from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Country
from .serializers import CountryCreateSerializator, CountrySerializator

# Create your views here.

class CountryAPIView(APIView):

    def get(self, request):
        countries = Country.objects.all()
        serializator = CountrySerializator(countries, many=True)

        return Response(serializator.data)

    def post(self, request):
        serializator = CountryCreateSerializator(data=request.data  )
        
        if serializator.is_valid():
            serializator.save()
            return Response(serializator.data)
        else:    
            return Response(status=400)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from .serializers import (CountrySerializator,
                          ProducerSerializtor,
                          CarSerializator,
                          CommentSerializator
                          )

from pandas import DataFrame


class CountryExportiew(APIView):

    def get(self, request):
        export = request.GET.get('export', False)

        if export:
            query = models.Country.objects.all()
            serializer = CountrySerializator(query, many=True)

            df = DataFrame(serializer.data)

            if export == 'csv':
                df.to_csv('static/export/csv/country.csv', encoding='UTF-8')
            elif export == 'xlsx':
                df.to_excel('static/export/xlsx/country.xlsx', encoding='UTF-8')
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)


class ProducerExportiew(APIView):

    def get(self, request):
        export = request.GET.get('export', False)

        if export:
            query = models.Producer.objects.all().select_related('country')
            serializer = ProducerSerializtor(query, many=True)

            df = DataFrame(serializer.data)

            if export == 'csv':
                df.to_csv('static/export/csv/producer.csv', encoding='UTF-8')
            elif export == 'xlsx':
                df.to_excel('static/export/xlsx/producer.xlsx', encoding='UTF-8')
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)
    

class CarExportiew(APIView):

    def get(self, request):
        export = request.GET.get('export', False)

        if export:
            query = models.Car.objects.all().select_related('producer')
            serializer = CarSerializator(query, many=True)

            df = DataFrame(serializer.data)

            if export == 'csv':
                df.to_csv('static/export/csv/car.csv', encoding='UTF-8')
            elif export == 'xlsx':
                df.to_excel('static/export/xlsx/car.xlsx', encoding='UTF-8')
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)
    

class CommentExportiew(APIView):

    def get(self, request):
        export = request.GET.get('export', False)

        if export:
            query = models.Comment.objects.all().select_related('car')
            serializer = CommentSerializator(query, many=True)

            df = DataFrame(serializer.data)

            if export == 'csv':
                df.to_csv('static/export/csv/comment.csv', encoding='UTF-8')
            elif export == 'xlsx':
                df.to_excel('static/export/xlsx/comment.xlsx', encoding='UTF-8')
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_200_OK)

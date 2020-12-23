from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Kicker
from .serializers import GetAllKickerSerializer, KickerSerializer


# Create your views here.


class infoKicker(APIView):

    def get(self, request):
        list_kickers = Kicker.objects.all()
        mydata = GetAllKickerSerializer(list_kickers, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    def post(self, request):
        mydata = KickerSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Sai DL', status=status.HTTP_400_BAD_REQUEST)
        name = mydata.data['name']
        dateOfBirth = mydata.data['dateOfBirth']
        height = mydata.data['height']
        number = mydata.data['number']
        image = mydata.data['image']

        k = Kicker.objects.create(
            name=name, dateOfBirth=dateOfBirth, height=height, number=number, image=image)
        return Response("ok", status=status.HTTP_200_OK)

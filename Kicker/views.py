from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework import status, mixins
from rest_framework import generics
from .models import Kicker
from .serializers import GetAllKickerSerializer, KickerSerializer


# Create your views here.

class KickerMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # queryset dùng để gọi method get_queryset() trong generics
    queryset = Kicker.objects.all()
    # serializer_class dùng để gọi method get_serializer_class() trong generics
    serializer_class = GetAllKickerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class infoKicker(APIView):
    def get(self, request):
        list_kickers = Kicker.objects.all()
        mydata = GetAllKickerSerializer(list_kickers, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    def post(self, request):
        kicker = GetAllKickerSerializer(data=request.data)
        if kicker.is_valid():
            kicker.save()
            return Response(data=kicker.data, status=status.HTTP_201_CREATED)
        return Response('Sai DL', status=status.HTTP_400_BAD_REQUEST)


class KickerInfo(APIView):

    def get_object(self, pk):
        try:
            return Kicker.objects.get(pk=pk)
        except:
            raise HttpResponse("Error 404")

    def get(self, request, pk):
        kicker = self.get_object(pk=pk)
        serializers = GetAllKickerSerializer(kicker)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        kicker = self.get_object(pk=pk)
        serializers = GetAllKickerSerializer(kicker, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response("NOT METHOD PUT", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        kicker = self.get_object(pk=pk)
        kicker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

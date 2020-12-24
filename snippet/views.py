from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import SnippetSerializer
from django.http import HttpResponse, JsonResponse
from .models import SnippetModel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = SnippetModel.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def list_snippets(request):
    if request.method == 'GET':
        snippets = SnippetModel.objects.all()
        serializers = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializers.data, safe=False)

    if request.method == 'POST':
        data = SnippetSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = SnippetModel.objects.get(pk=pk)
    except SnippetModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse(status=204)

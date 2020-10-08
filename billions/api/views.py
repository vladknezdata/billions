from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReferenceSerializer
from references.models import Reference

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': 'task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>'
    }

    return Response(api_urls)

@api_view(["GET"])
def referenceList(request):
    references = Reference.objects.all()
    serializer = ReferenceSerializer(references, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def referenceDetail(request, pk):
    references = Reference.objects.get(id=pk)
    serializer = ReferenceSerializer(references, many=False)
    return Response(serializer.data)
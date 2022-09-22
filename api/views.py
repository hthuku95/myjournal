from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from rest_framework import status
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request,format=None):

    routes = [
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of Note objects'
        },
        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single Note object'
        },
        {
            'Endpoint':'/notes/create',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates a single Note object with the data sent by the post request'
        },
        {
            'Endpoint':'/notes/id/update',
            'method':'PUT',
            'body':{'body':""},
            'description':'Updates an existing Note object with the data sent by the put request ',
        },
        {
            'Endpoint':'/notes/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing Note object'
        }
    ]

    return Response(routes)


@api_view(['GET','POST'])
def getNotes(request,format=None):

    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','DELETE'])
def getNote(request,pk,format=None):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.mehod == 'GET':
        serializer = NoteSerializer(note,many=False)
        return Response(serializer.data)
    elif requst.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def updateNote(request,pk,format=None):
    # POST Data
    data = request.data

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note,data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

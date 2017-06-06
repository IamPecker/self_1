from root.models import Room
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from django.utils import timezone

class RoomSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(min_length=1)

    class Meta:
        model = Room
        fields = '__all__'


@api_view(['GET', 'POST'])
def room(request):
    if request.method == 'GET':
        room_list = Room.objects.order_by('id')
        serializer = RoomSerializer(room_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RoomSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.sava()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT',])
def room_ch(request, id):
    room_change = Room.objects.get(id = id)
    if request.method == 'PUT':
        dat = request.data.copy()
        time = timezone.now()
        dat.__setitem__(key='time_use', value=time)
        serializer = RoomSerializer(room_change, data=dat)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

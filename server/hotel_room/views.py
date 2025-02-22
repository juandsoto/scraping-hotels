from django.views.decorators.csrf import csrf_exempt 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def get_hotel_rooms(request):
    try:
        rooms = HotelRoom.objects.all().order_by('id')
        serializer = HotelRoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except HotelRoom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except BaseException:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@csrf_exempt
@api_view(['GET'])
def get_hotel_room(request, room_id):
    try:    
        room = HotelRoom.objects.get(pk=room_id)
        serializer = HotelRoomSerializer(room)
        return Response(serializer.data)
    except HotelRoom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except BaseException:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
def create_hotel_room(request):
    serializer = HotelRoomCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PATCH'])
def modify_hotel_room(request, room_id):
    try:
        room = HotelRoom.objects.get(pk=room_id)
    except HotelRoom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = HotelRoomSerializer(room, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def delete_hotel_room(request, room_id):
    try:
        room = HotelRoom.objects.get(pk=room_id)
        room.delete()
        return Response(status=status.HTTP_200_OK)
    except HotelRoom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except BaseException:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
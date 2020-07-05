from django.db.models import Min
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Room, IntervalData
from .serializer import RoomSerializer
from django.utils.dateparse import parse_datetime
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def findAvailableRooms(request):
    permission_classes = (IsAuthenticated,)
    try:
        bookingdata = json.loads(request.body)
        number = bookingdata["numberofpeople"]
        between = bookingdata["between"]

        roomNumber = checkAvailability(number,between)

        if(roomNumber==None):
            return JsonResponse("Not Available Room in this building", safe=False)

        resp_data = {'options':{'RoomId':roomNumber,'Between':between}}

        return JsonResponse(resp_data,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def bookRoom(request):
    try:
        bookingdata = json.loads(request.body)
        number = bookingdata["Numberofpeople"]
        between = bookingdata["Between"]
        roomId = bookingdata["Roomid"]

        roomNumber = checkAvailability(number,between)

        response = bookRoom(roomId, between, roomNumber, True)

        if(response==None):
            return JsonResponse("Please find another building", safe=False)

        resp_data = {'Response':"Success"}

        return JsonResponse(resp_data,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


def bookRoom(number, between, roomNumber, roomAvailable):

    isSuccess = False
    bookRoom(roomNumber,between)
    if(roomAvailable==True):
      intervalData = IntervalData(fromTime= parse_datetime(between[0]),toTime=parse_datetime(between[1]))
      roomData = Room.objects.get(roomid=roomNumber)
      roomData.max_numberofpeople = roomData.max_numberofpeople - number
      intervalData.roomidstored = roomData
      intervalData.save()
      roomData.save()
      isSuccess = True
    else:
      roomNumber = None
      isSuccess = False

    return isSuccess


def checkAvailability(number, between):

    raw_data = Room.objects.values_list('roomid', 'max_numberofpeople').order_by('max_numberofpeople')
    roomAvailable = False

    notAvalaibleRooms = []

    roomData = Room.objects.all()
    for room in roomData:
        listIntervalData = IntervalData(fromTime=parse_datetime(between[0]), toTime=parse_datetime(between[1]))
        listIntervalData.roomidstored = room
        intervalRoomId = listIntervalData.roomidstored.roompickup.all()
        for iter in intervalRoomId:
            if (parse_datetime(between[0]).replace(tzinfo=None) >= iter.fromTime.replace(tzinfo=None) and parse_datetime(
                    between[0]) <= iter.toTime.replace(tzinfo=None)):
                if (parse_datetime(between[1]) >= iter.fromTime.replace(tzinfo=None) and parse_datetime(
                        between[1]) <= iter.toTime.replace(tzinfo=None)):
                    notAvalaibleRooms.append(room.roomid)

    naRooms = set(notAvalaibleRooms)

    for roomid, max_numberofpeople in raw_data:
        if (max_numberofpeople != None and number <= max_numberofpeople):
            roomNumber = roomid

            if(len(naRooms) == 0):
                roomAvailable = True
                break

            for naRoom in naRooms:
                if(not naRoom == roomNumber):
                    roomAvailable = True
                    break

    if(roomAvailable==True):
      intervalData = IntervalData(fromTime= parse_datetime(between[0]),toTime=parse_datetime(between[1]))
      roomData = Room.objects.get(roomid=roomNumber)
      roomData.max_numberofpeople = roomData.max_numberofpeople - number
      intervalData.roomidstored = roomData
      intervalData.save()
      roomData.save()
    else:
      roomNumber = None

    return roomNumber

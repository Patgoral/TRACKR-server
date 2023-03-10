from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.attendee import Attendee
from ..serializers import AttendeeSerializer, AttendeeWriteSerializer

class Attendees(generics.ListCreateAPIView):

    queryset = ()
    serializer_class = AttendeeSerializer

    def get(self, request):
        """Index request"""
        # FILTER only shows user's created items
        attendees = Attendee.objects.filter(owner=request.user)
        serializer = AttendeeSerializer(attendees, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create request"""
        request.data._mutable = True
        request.data["owner"] = request.user.id
        serializer = AttendeeWriteSerializer(data=request.data)
        if serializer.is_valid():
            m = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendeeDetail(generics.ListCreateAPIView):
    serializer_class = AttendeeSerializer

    def get(self, request, pk):
        """Show request"""
        attendee = get_object_or_404(Attendee, pk=pk)
        serializer = AttendeeSerializer(attendee)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Delete request"""
        attendee = get_object_or_404(Attendee, pk=pk)
        if request.user != attendee.owner:
            raise PermissionDenied('Unauthorized Access')
        
        attendee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """Update Request"""
        attendee = get_object_or_404(Attendee, pk=pk)
        if request.user != attendee.owner:
            raise PermissionDenied('You do not own this attendee')
        # Validate updates with serializer
        serializer = AttendeeSerializer(attendee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
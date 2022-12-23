from rest_framework import viewsets
from .models import *
from .serializers import *

class ChoristesViewSet(viewsets.ModelViewSet):
    queryset = Choriste.objects.all()
    serializer_class = ChoristesSerializer
    
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

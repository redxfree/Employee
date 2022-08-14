from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import *
from .serializers import *
	

class ListView(generics.ListAPIView):
	queryset = Employee.objects.all()
	serializer_class = CustomRegisterSerializer
	
class Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Employee.objects.all()
	serializer_class = CustomUserDetailsSerializer
 
class Material(generics.CreateAPIView):
	queryset = Material.objects.all()
	serializer_class = Materialserailizer
	


class Attendance(generics.CreateAPIView):
	queryset = Attendance.objects.all()
	serializer_class = Attendanceserializer
	


class Transport(generics.CreateAPIView):
	queryset = Transport.objects.all()
	serializer_class = Transportserailizer
	

class Leave(generics.CreateAPIView):
	queryset = Leave.objects.all()
	serializer_class = Leaveserailizer
	


class Overtime(generics.CreateAPIView):
	queryset = OverTime.objects.all()
	serializer_class = Overtimeserailizer
	
		

class Appraisalstep(generics.CreateAPIView):
	queryset = ApprasialStep.objects.all()
	serializer_class = Appraisalstepserializer
	


class AppraisalResult(generics.CreateAPIView):
	queryset = ApprasialResult.objects.all()
	serializer_class = Appraisalresultserializer
	


class Appraisa(generics.CreateAPIView):
	queryset = Apprasial.objects.all()
	serializer_class = Apprasialserializer
	

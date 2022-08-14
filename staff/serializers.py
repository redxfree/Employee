from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields =  ['department']


class DesignationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Designation
		fields = ['designation']
		

class CustomRegisterSerializer(RegisterSerializer):
	gender = serializers.ChoiceField(choices=GENDERS)
	contact = serializers.IntegerField()
	employee_image  = serializers.ImageField()
	salary = serializers.IntegerField()
	age = serializers.IntegerField()
	department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
	designation = serializers.PrimaryKeyRelatedField(queryset=Designation.objects.all())
	dob = serializers.DateField()
	joining_date = serializers.DateField()
	exit_date = serializers.DateField()
	
	# Define transaction.atomic to rollback the save operation in case of error
	@transaction.atomic
	def save(self, request):
		user = super().save(request)
		user.gender = self.data.get('gender')
		user.contact = self.data.get('contact')
		user.age = self.data.get('age')
		user.employee_image = self.data.get('employee_image')
		user.salary = self.data.get('salary')
		user.joining_date = self.data.get('joining_date')
		user.dob = self.data.get('dob')
		user.exit_date = self.data.get('exit_date')
		
		user.save()
		return user
	
	
	

class CustomUserDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = '__all__'


class Overtimeserailizer(serializers.ModelSerializer):
	class Meta:
		model  = OverTime
		fields = '__all__'
  
		
	
class Attendanceserializer(serializers.ModelSerializer):
	class Meta:
		model = Attendance
		fields = '__all__'
  
  
class Apprasialserializer(serializers.ModelSerializer):
	class Meta:
		model = Apprasial
		fields = '__all__'
		
	
class Appraisalstepserializer(serializers.ModelSerializer):
	class Meta:
		model  = ApprasialStep
		fields = '__all__'
		
	
	
class Appraisalresultserializer(serializers.ModelSerializer):
	class Meta:
		model = ApprasialResult
		fields = '__all__'
		
class AvailabelMaterialserializer(serializers.ModelSerializer):
	class Meta:
		model = AvailableMaterial
		fields = '__all__'
		
class Materialserailizer(serializers.ModelSerializer):
	class Meta:
		model  = Material
		fields  = '__all__'
		
class Transportserailizer(serializers.ModelSerializer):
	class Meta:
		model = Transport
		fields = '__all__'
		
class Leaveserailizer(serializers.ModelSerializer):
	class Meta:
		model = Leave
		fields = '__all__'
		

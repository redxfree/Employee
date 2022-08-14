
from django.urls import path
from .views import *





urlpatterns = [
    path('list/',ListView.as_view(),name='list'),
	path('detail/<int:pk>/',Detail.as_view(),name='detail'),
	path('attendance/',Attendance.as_view(),name='attendance'),
	path('material/',Material.as_view(),name='material'),
	path('transport/',Transport.as_view(),name='transport'),
	path('overtime/',Overtime.as_view(),name='overtime'),
	path('leave/',Leave.as_view(),name='leave'),
	path('appraisal/',Appraisa.as_view(),name='appraisal'),
	path('step/',Appraisalstep.as_view(),name='step'),
	path('result/',AppraisalResult.as_view(),name='result'),
    
]

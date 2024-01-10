from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView, UpdateAPIView
from accounts.models import Account
from courses.models import Course
from courses.serializers import ListAddStudentCourseSerializer
from students_courses.permissions import IsSuperuser
from students_courses.serializers import StudentCourseSerializer

class ListStudentCourseView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    queryset = Course.objects.all()
    serializer_class = ListAddStudentCourseSerializer
    lookup_url_kwarg = "course_id"

class UpdateStudentCourseView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    queryset = Course.objects.all()
    serializer_class = ListAddStudentCourseSerializer
    lookup_url_kwarg = "course_id"

  
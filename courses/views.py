from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.models import Course
from courses.serializers import ListCreateCourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperuserOrReadOnly
from rest_framework.response import Response
from rest_framework import status

class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = ListCreateCourseSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return self.queryset.all()

class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = ListCreateCourseSerializer
    lookup_url_kwarg = "course_id"

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return self.queryset.all()


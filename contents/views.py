from django.shortcuts import render
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from contents.models import Content
from contents.serializers import ContentSerializer
from courses.models import Course

from courses.permissions import IsSuperuserOrReadOnly

class CreateContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = Course.objects.filter(pk=self.kwargs['course_id']).first()
        if not course:
            raise NotFound({'detail': "course not found."})
        serializer.save(course=course)

class RetriveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]
    # queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_queryset(self):
        course = Course.objects.filter(pk=self.kwargs['course_id']).first()
        if not course:
            raise NotFound({'detail': "course not found."})
        content= Content.objects.filter(pk=self.kwargs['content_id']).first()
        if not content:
            raise NotFound({"detail": "content not found."})
        # if not self.request.user.is_superuser:
        #     return Course.objects.filter(students=self.request.user)
        # return self.queryset.all()
        user = self.request.user
        if user.is_superuser:
            # Superusuário tem permissão total
            return Content.objects.all()

        # Verifica se o usuário está matriculado no curso associado ao conteúdo
        course = content.course
        if user in course.students.all():
            return Content.objects.filter(course=course)
        else:
            raise PermissionDenied({"detail": "You do not have permission to perform this action."})

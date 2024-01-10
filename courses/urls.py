
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from contents.views import CreateContentView, RetriveUpdateDestroyContentView
from courses.views import ListCreateCourseView, RetrieveUpdateDestroyCourseView
from students_courses.views import ListStudentCourseView, UpdateStudentCourseView


urlpatterns = [
    path("courses/", ListCreateCourseView.as_view()),
    path("courses/<str:course_id>/", RetrieveUpdateDestroyCourseView.as_view()),
    path("courses/<str:course_id>/contents/", CreateContentView.as_view()),
    path("courses/<str:course_id>/contents/<str:content_id>/", RetriveUpdateDestroyContentView.as_view()),
    # path("courses/<str:course_id>/students/", ListStudentCourseView.as_view()),
     path("courses/<str:course_id>/students/", UpdateStudentCourseView.as_view()),
    
]
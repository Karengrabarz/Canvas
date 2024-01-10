from rest_framework import serializers
from rest_framework.response import Response

from accounts.models import Account
from .models import Course
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer 
from rest_framework.validators import UniqueValidator

class ListCreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'status', 'start_date', 'end_date', 'instructor','contents', 'students_courses' ]
        extra_kwargs = {
            # 'name': {'validators':[UniqueValidator(queryset=Course.objects.all(),message="course with this name already exists.")]},
            'contents': {'read_only':True},
            'students_courses':{'read_only':True}
        }
class ListAddStudentCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id','name','students_courses']
        extra_kwargs = {
        'id': {'read_only':True},
        'name': {'read_only':True}
        }
    def update(self, instance, validated_data):
        course = instance
        students_courses = validated_data['students_courses']
        student_found = []
        student_not_found = []
        for student_course_data in students_courses:
            student_email = student_course_data.get('student').get('email')
            try:
                student = Account.objects.get(email=student_email)
                student_found.append(student)
            except Account.DoesNotExist:
                student_not_found.append(student_email)

        if student_not_found:
            raise serializers.ValidationError({
                "detail": f"No active accounts was found: { ", ".join(student_not_found) }."
            })       
        if not self.partial:
            course.students.add(*student_found)
        return instance

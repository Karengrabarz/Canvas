from .models import StudentCourse
from rest_framework import serializers

class StudentCourseSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source='student.id',read_only=True)
    student_username = serializers.CharField(source='student.username',read_only=True)
    student_email = serializers.CharField(source='student.email')
    class Meta:
        model = StudentCourse
        fields = ['id', 'status','student_id', 'student_username', 'student_email']
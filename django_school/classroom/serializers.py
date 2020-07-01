from classroom.models import Quiz, Subject, User
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject
    fields = ['name', 'color']


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_student', 'is_teacher']


class QuizSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    owner = UserSerializer()
    class Meta:
        model = Quiz
        fields = ['owner', 'name', 'subject']

from django import forms
from django.db import transaction

from schools.forms import CustomUserCreationForm
from classroom.models import ClassRoom
from quizzes.models import Subject
from schools.models import AcademicYear

from .models import Student, StudentMigration

class StudentSignUpForm(CustomUserCreationForm):
    classroom = forms.CharField(required=True,
        widget=forms.Select(attrs={'required': 'required'}))
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     required=True
    # )
    
    def clean_classroom(self):
        # print (self.cleaned_data['classroom'])
        return self.cleaned_data['classroom']

    @transaction.atomic
    def save(self):
        classroom = ClassRoom.objects.get(id= self.cleaned_data.get('classroom'))
        academicyear = AcademicYear.objects.get(status=True)     

        user = super().save(commit=False)
        user.user_type = 1 # student
        #user.is_active = False
        #user.school = self.cleaned_data.get('school')
        user.save()
        
        student = Student.objects.create(user=user,classroom = classroom)
        StudentMigration.objects.create(student = student, classroom = classroom, academicyear = academicyear)
        # student.interests.add(*self.cleaned_data.get('interests'))        
        # course.students.add(user)
        return user

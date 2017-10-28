from django import forms
from .models import Student, Course, CourseObject, UserInfo, Contract, ContractEndInfo


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['school', 'name', 'grade', 'letter', 'passportserialnumber', 'passportissued', 'homeaddress', 'phone', 'parentname', 'parentpassportserialnumber', 'parentpassportissued', 'parentinn', 'parenthomeaddress', 'parentphone', 'created']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['direction', 'name', 'priceforanhour', 'numberofhours', 'numberofmounths', 'countinaweek']


class CourseObjectForm(forms.ModelForm):
    class Meta:
        model = CourseObject
        fields = ['timemask', 'course', 'teacher']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'typeofuser', 'user']


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['number', 'status', 'student', 'courseobject']


class ContractEndInfoForm(forms.ModelForm):
    class Meta:
        model = ContractEndInfo
        fields = ['date', 'numberofhoursworked', 'contract']


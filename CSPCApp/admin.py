from django.contrib import admin
from django import forms
from .models import Student, Course, CourseObject, UserInfo, Contract, ContractEndInfo

class StudentAdminForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = ['school', 'name', 'grade', 'letter', 'passportserialnumber', 'passportissued', 'homeaddress', 'phone', 'parentname', 'parentpassportserialnumber', 'parentpassportissued', 'parentinn', 'parenthomeaddress', 'parentphone', 'created']
    # readonly_fields = ['school', 'name', 'grade', 'letter', 'passportserialnumber', 'passportissued', 'homeaddress', 'phone', 'parentname', 'parentpassportserialnumber', 'parentpassportissued', 'parentinn', 'parenthomeaddress', 'parentphone', 'created']

admin.site.register(Student, StudentAdmin)


class CourseAdminForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ['direction', 'name', 'priceforanhour', 'numberofhours', 'numberofmounths', 'countinaweek']
    # readonly_fields = ['direction', 'name', 'priceforanhour', 'numberofhours', 'numberofmounths', 'countinaweek']

admin.site.register(Course, CourseAdmin)


class CourseObjectAdminForm(forms.ModelForm):

    class Meta:
        model = CourseObject
        fields = '__all__'


class CourseObjectAdmin(admin.ModelAdmin):
    form = CourseObjectAdminForm
    list_display = ['timemask']
    # readonly_fields = ['timemask']

admin.site.register(CourseObject, CourseObjectAdmin)


class UserInfoAdminForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = '__all__'


class UserInfoAdmin(admin.ModelAdmin):
    form = UserInfoAdminForm
    list_display = ['name', 'typeofuser']
    # readonly_fields = ['name', 'typeofuser']

admin.site.register(UserInfo, UserInfoAdmin)


class ContractAdminForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = '__all__'


class ContractAdmin(admin.ModelAdmin):
    form = ContractAdminForm
    list_display = ['number', 'status']
    # readonly_fields = ['number', 'status']

admin.site.register(Contract, ContractAdmin)


class ContractEndInfoAdminForm(forms.ModelForm):

    class Meta:
        model = ContractEndInfo
        fields = '__all__'


class ContractEndInfoAdmin(admin.ModelAdmin):
    form = ContractEndInfoAdminForm
    list_display = ['date', 'numberofhoursworked']
    # readonly_fields = ['date', 'numberofhoursworked']

admin.site.register(ContractEndInfo, ContractEndInfoAdmin)
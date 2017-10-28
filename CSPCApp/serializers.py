from . import models

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = (
            'pk',
            'school',
            'name',
            'grade',
            'letter',
            'passportserialnumber',
            'passportissued',
            'homeaddress',
            'phone',
            'parentname',
            'parentpassportserialnumber',
            'parentpassportissued',
            'parentinn',
            'parenthomeaddress',
            'parentphone',
            'created',
        )


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = (
            'pk',
            'direction',
            'name',
            'priceforanhour',
            'numberofhours',
            'numberofmounths',
            'countinaweek',
        )


class CourseObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CourseObject
        fields = (
            'pk',
            'timemask',
        )


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserInfo
        fields = (
            'pk',
            'name',
            'typeofuser',
        )


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contract
        fields = (
            'pk',
            'number',
            'status',
        )


class ContractEndInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContractEndInfo
        fields = (
            'pk',
            'date',
            'numberofhoursworked',
        )



from . import models
from . import serializers
from rest_framework import viewsets, permissions


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Student class"""

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course class"""

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseObjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the CourseObject class"""

    queryset = models.CourseObject.objects.all()
    serializer_class = serializers.CourseObjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserInfo class"""

    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContractViewSet(viewsets.ModelViewSet):
    """ViewSet for the Contract class"""

    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContractEndInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the ContractEndInfo class"""

    queryset = models.ContractEndInfo.objects.all()
    serializer_class = serializers.ContractEndInfoSerializer
    permission_classes = [permissions.IsAuthenticated]



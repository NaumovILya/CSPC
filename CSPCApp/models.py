from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db import fields as extension_fields
from django.utils import timezone


class Student(models.Model):

    # Fields
    school = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    grade = models.SmallIntegerField()
    letter = models.CharField(max_length=2)
    passportserialnumber = models.BigIntegerField()
    passportissued = models.CharField(max_length=128)
    homeaddress = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    parentname = models.CharField(max_length=64)
    parentpassportserialnumber = models.BigIntegerField()
    parentpassportissued = models.CharField(max_length=128)
    parentinn = models.BigIntegerField()
    parenthomeaddress = models.CharField(max_length=128)
    parentphone = models.BigIntegerField()
    created = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('CSPCApp_student_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('CSPCApp_student_update', args=(self.pk,))


class Course(models.Model):

    # Fields
    direction = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    priceforanhour = models.SmallIntegerField()
    numberofhours = models.SmallIntegerField()
    numberofmounths = models.SmallIntegerField()
    countinaweek = models.SmallIntegerField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('CSPCApp_course_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('CSPCApp_course_update', args=(self.pk,))


class CourseObject(models.Model):

    # Fields
    timemask = models.BigIntegerField()

    # Relationship Fields
    course = models.ForeignKey('CSPCApp.Course', )
    teacher = models.ForeignKey('CSPCApp.UserInfo', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('CSPCApp_courseobject_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('CSPCApp_courseobject_update', args=(self.pk,))


class UserInfo(models.Model):

    # Fields
    name = models.CharField(max_length=64)
    typeofuser = models.SmallIntegerField()

    # Relationship Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('CSPCApp_userinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('CSPCApp_userinfo_update', args=(self.pk,))


class Contract(models.Model):

    # Fields
    number = models.BigIntegerField()
    status = models.SmallIntegerField()

    # Relationship Fields
    student = models.ForeignKey('CSPCApp.Student', )
    courseobject = models.ForeignKey('CSPCApp.CourseObject', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('CSPCApp_contract_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('CSPCApp_contract_update', args=(self.pk,))


class ContractEndInfo(models.Model):

    # Fields
    date = models.DateField(default=timezone.now)
    numberofhoursworked = models.SmallIntegerField()

    # Relationship Fields
    contract = models.ForeignKey('CSPCApp.Contract', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('CSPCApp_contractendinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('CSPCApp_contractendinfo_update', args=(self.pk,))



from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Student, Course, CourseObject, UserInfo, Contract, ContractEndInfo
from .forms import StudentForm, CourseForm, CourseObjectForm, UserInfoForm, ContractForm, ContractEndInfoForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm


class CourseListView(ListView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm


class CourseDetailView(DetailView):
    model = Course


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm


class CourseObjectListView(ListView):
    model = CourseObject


class CourseObjectCreateView(CreateView):
    model = CourseObject
    form_class = CourseObjectForm


class CourseObjectDetailView(DetailView):
    model = CourseObject


class CourseObjectUpdateView(UpdateView):
    model = CourseObject
    form_class = CourseObjectForm


class UserInfoListView(ListView):
    model = UserInfo


class UserInfoCreateView(CreateView):
    model = UserInfo
    form_class = UserInfoForm


class UserInfoDetailView(DetailView):
    model = UserInfo


class UserInfoUpdateView(UpdateView):
    model = UserInfo
    form_class = UserInfoForm


class ContractListView(ListView):
    model = Contract


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm


class ContractDetailView(DetailView):
    model = Contract


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm


class ContractEndInfoListView(ListView):
    model = ContractEndInfo


class ContractEndInfoCreateView(CreateView):
    model = ContractEndInfo
    form_class = ContractEndInfoForm


class ContractEndInfoDetailView(DetailView):
    model = ContractEndInfo


class ContractEndInfoUpdateView(UpdateView):
    model = ContractEndInfo
    form_class = ContractEndInfoForm


@login_required
def mainPage(request):
    return render(request, 'CSPCApp/mainPage.html')

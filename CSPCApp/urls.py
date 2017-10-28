from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'student', api.StudentViewSet)
router.register(r'course', api.CourseViewSet)
router.register(r'courseobject', api.CourseObjectViewSet)
router.register(r'userinfo', api.UserInfoViewSet)
router.register(r'contract', api.ContractViewSet)
router.register(r'contractendinfo', api.ContractEndInfoViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Student

    url(r'^CSPCApp/student/$', views.StudentListView.as_view(), name='CSPCApp_student_list'),
    url(r'^CSPCApp/student/create/$', views.StudentCreateView.as_view(), name='CSPCApp_student_create'),
    url(r'^CSPCApp/student/detail/(?P<pk>\S+)/$', views.StudentDetailView.as_view(), name='CSPCApp_student_detail'),
    url(r'^CSPCApp/student/update/(?P<pk>\S+)/$', views.StudentUpdateView.as_view(), name='CSPCApp_student_update'),
)

urlpatterns += (
    # urls for Course
    url(r'^CSPCApp/course/$', views.CourseListView.as_view(), name='CSPCApp_course_list'),
    url(r'^CSPCApp/course/create/$', views.CourseCreateView.as_view(), name='CSPCApp_course_create'),
    url(r'^CSPCApp/course/detail/(?P<pk>\S+)/$', views.CourseDetailView.as_view(), name='CSPCApp_course_detail'),
    url(r'^CSPCApp/course/update/(?P<pk>\S+)/$', views.CourseUpdateView.as_view(), name='CSPCApp_course_update'),
)

urlpatterns += (
    # urls for CourseObject
    url(r'^CSPCApp/courseobject/$', views.CourseObjectListView.as_view(), name='CSPCApp_courseobject_list'),
    url(r'^CSPCApp/courseobject/create/$', views.CourseObjectCreateView.as_view(), name='CSPCApp_courseobject_create'),
    url(r'^CSPCApp/courseobject/detail/(?P<pk>\S+)/$', views.CourseObjectDetailView.as_view(), name='CSPCApp_courseobject_detail'),
    url(r'^CSPCApp/courseobject/update/(?P<pk>\S+)/$', views.CourseObjectUpdateView.as_view(), name='CSPCApp_courseobject_update'),
)

urlpatterns += (
    # urls for UserInfo
    url(r'^CSPCApp/userinfo/$', views.UserInfoListView.as_view(), name='CSPCApp_userinfo_list'),
    url(r'^CSPCApp/userinfo/create/$', views.UserInfoCreateView.as_view(), name='CSPCApp_userinfo_create'),
    url(r'^CSPCApp/userinfo/detail/(?P<pk>\S+)/$', views.UserInfoDetailView.as_view(), name='CSPCApp_userinfo_detail'),
    url(r'^CSPCApp/userinfo/update/(?P<pk>\S+)/$', views.UserInfoUpdateView.as_view(), name='CSPCApp_userinfo_update'),
)

urlpatterns += (
    # urls for Contract
    url(r'^CSPCApp/contract/$', views.ContractListView.as_view(), name='CSPCApp_contract_list'),
    url(r'^CSPCApp/contract/create/$', views.ContractCreateView.as_view(), name='CSPCApp_contract_create'),
    url(r'^CSPCApp/contract/detail/(?P<pk>\S+)/$', views.ContractDetailView.as_view(), name='CSPCApp_contract_detail'),
    url(r'^CSPCApp/contract/update/(?P<pk>\S+)/$', views.ContractUpdateView.as_view(), name='CSPCApp_contract_update'),
)

urlpatterns += (
    # urls for ContractEndInfo
    url(r'^CSPCApp/contractendinfo/$', views.ContractEndInfoListView.as_view(), name='CSPCApp_contractendinfo_list'),
    url(r'^CSPCApp/contractendinfo/create/$', views.ContractEndInfoCreateView.as_view(), name='CSPCApp_contractendinfo_create'),
    url(r'^CSPCApp/contractendinfo/detail/(?P<pk>\S+)/$', views.ContractEndInfoDetailView.as_view(), name='CSPCApp_contractendinfo_detail'),
    url(r'^CSPCApp/contractendinfo/update/(?P<pk>\S+)/$', views.ContractEndInfoUpdateView.as_view(), name='CSPCApp_contractendinfo_update'),
    url(r'^', views.mainPage, name='mainPage'),
)


from django.urls import path,include
from . import views
from rest_framework . routers import DefaultRouter
from . views import Studentt,Employeee



router=DefaultRouter()
router.register(r'student',Studentt,basename='student')
router.register(r'employee',Employeee,basename='employee')


urlpatterns=[
    path('home/',views.home),
    path('',include(router.urls)),
    path('home/',views.home),
    path('about/',views.about),
    path('course/',views.course),
    path('features/',views.features),
]
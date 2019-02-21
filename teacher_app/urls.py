
from django.urls import path,include
from . import views

urlpatterns = [

    path('all_teachers',views.All_Teacher,name='all_teacher'),
    path('add_teacher',views.Add_Teacher,name='add_teacher'),
    path('teacher_info',views.Teacher_Info,name='teacher_info'),
]

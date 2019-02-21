
from django.urls import path,include
from . import views

urlpatterns = [
    path('students',views.studentall,name='studentall'),
    path('new_student',views.new_student,name='new_student'),
    path('add_student',views.Add_Student,name='add_student'),
    path('student_info/<int:id>',views.studentInfo,name='student_info'),
    path('student_update/<int:id>',views.Student_Update,name='student_update'),
    path('student_fees',views.StudentFees_collection,name='student_fees'),
    path('Add_Student_fees',views.Student_fees_form,name='Add_Student_fees')
]

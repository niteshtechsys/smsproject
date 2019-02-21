from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def All_Teacher(request):
    return render(request,"./teacher/all_teacher.html")

def Add_Teacher(request):
    return render(request,"./teacher/add_professor.html")

def Teacher_Info(request):
    return render(request,"./teacher/professor_info.html")

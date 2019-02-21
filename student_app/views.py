from django.shortcuts import render,redirect
from . models import Student
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def new_student(request):
    return render(request,'student/add_student.html')

def studentall(request):
    student_list = Student.objects.all()
    return render(request,"./student/student_all.html",{'student_list':student_list})

def Add_Student(request):
    if request.method =="POST":
        student_name = request.POST['student_name']
        student_lname = request.POST['student_lname']
        student_reg_date = request.POST['reg_date']
        class_name = request.POST['class_name']
        Student_gender = request.POST['gender']
        student_Mobile = request.POST['Mobile']
        student_parents_name = request.POST['parents_name']
        student_parents_mob_number = request.POST['parents_mob_number']
        student_dob = request.POST['dob']
        student_blood_group = request.POST['blood_group']
        student_address = request.POST['addr']
        student_rti = request.POST.get('RTI', False)
        student_sibling = request.POST.get('sibling', False)
        student_sib_class = request.POST['sib_class']
        student_sib_rel = request.POST['sib_rel']
        student_sib_mob = request.POST['sib_mob']
        student_sib_name = request.POST['sib_name']
        student_fees_options = request.POST['options']
        student_fees_amt = request.POST['fees_amt']
        student_ref_no = request.POST['ref_no']
        student_pay_type = request.POST['pay_type']
        student_pay_stutus = request.POST['pay_stutus']
        student_pay_detail = request.POST['pay_detail']

        new_student = Student(
			student_name=student_name,
			student_lastname=student_lname,
			Registration_date=student_reg_date,
			class_name=class_name,
			gender_type=Student_gender,
			mob_number=student_Mobile,
			parents_name=student_parents_name,
			parents_phone=student_parents_mob_number,
			Birth_date=student_dob,
			Blood_group=student_blood_group,
			address=student_address,
            rti=student_rti,
			sibling=student_sibling,
			sib_class_name=student_sib_class,
			sib_rel_name=student_sib_rel,
			sib_phone=student_sib_mob,
			sib_name=student_sib_name,
			pay_choice=student_fees_options,
			fees_amount=student_fees_amt,
			ref_number=student_ref_no,
			pay_type=student_pay_type,
			pay_status=student_pay_stutus,
			pay_details=student_pay_detail,
			)
        new_student.save()
        return redirect('/new_student')

def Student_Update(request,id):
    student_edit = Assets.objects.get(id=id)
    return render(request,"./student/student_update.html",{'student_edit':student_edit})

def studentInfo(request,id):
    student_info = Student.objects.get(id=id)
    return render(request,"./student/student_profile.html",{'student_info':student_info})

def StudentFees_collection(request):
    return render(request,"./fees/fees_collection.html")

def Student_fees_form(request):
    return render(request,"./fees/fees_form.html")

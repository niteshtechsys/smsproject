from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Holiday
from . models import Assets
from django.core.paginator import Paginator
from django.utils.crypto import get_random_string


def index(request):
    holiday_obj = Holiday.objects.all()
    paginator = Paginator(holiday_obj, 5)
    page = request.GET.get('page')
    holiday_list = paginator.get_page(page)
    return render(request,'index.html',{'holiday_list':holiday_list})

def All_Asset(request):
    all_assets = Assets.objects.all()
    return render(request,"./inventory/all_assets.html",{'all_assets':all_assets})

def Add_Asset(request):
    ref_number = get_random_string(length=7)
    return render(request,"./inventory/add_asset.html",{'ref_number':ref_number})

def Insert_Asset(request):
    if request.method == "POST":
        asset_name = request.POST['asset_name']
        asset_dep = request.POST['asset_dep']
        vendor_name = request.POST['vendor_name']
        receiver_name = request.POST['receiver_name']
        class_name = request.POST['class_name']
        asset_type = request.POST['asset_type']
        purchase_date = request.POST['purchase_date']
        amount = request.POST['amount']
        pay_status = request.POST['pay_status']
        ref_number = request.POST['ref_number']
        asset_details = request.POST['asset_details']

        Assets_new = Assets(
			asset_name=asset_name,
			asset_dep=asset_dep,
			vendor_name=vendor_name,
			receiver_name=receiver_name,
			class_name=class_name,
			asset_type=asset_type,
			purchase_date=purchase_date,
			amount=amount,
			pay_status=pay_status,
			ref_number=ref_number,
			asset_details=asset_details,
			)
        Assets_new.save()
        return redirect('/add_new_asset')

def Edit_Asset(request,id):
    assets_edit = Assets.objects.get(id=id)
    return render(request,"./inventory/asset_update.html",{'assets_edit':assets_edit})

def Update_Asset(request,id):
    if request.method == "POST":
        asset_name = request.POST['asset_name']
        asset_dep = request.POST['asset_dep']
        vendor_name = request.POST['vendor_name']
        receiver_name = request.POST['receiver_name']
        class_name = request.POST['class_name']
        asset_type = request.POST['asset_type']
        purchase_date = request.POST['purchase_date']
        amount = request.POST['amount']
        pay_status = request.POST['pay_status']
        ref_number = request.POST['ref_number']
        asset_details = request.POST['asset_details']
        print(asset_details)

        user_update = Assets.objects.filter(id=id).update(
		        asset_name=asset_name,
      			asset_dep=asset_dep,
      			vendor_name=vendor_name,
      			receiver_name=receiver_name,
      			class_name=class_name,
      			asset_type=asset_type,
      			purchase_date=purchase_date,
      			amount=amount,
      			pay_status=pay_status,
      			ref_number=ref_number,
      			asset_details=asset_details,
		)
        return redirect('/all_asset')

def Asset_Info(request,id):
    assets_info = Assets.objects.get(id=id)
    return render(request,"./inventory/asset_info.html",{'assets_info':assets_info})

def Asset_Delete(request,id):
    asset_del = Assets.objects.get(id=id)
    asset_del.delete()
    return redirect('/all_asset')

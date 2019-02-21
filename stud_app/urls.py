from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('all_asset',views.All_Asset,name='all_asset'),
    path('add_new_asset',views.Add_Asset,name='add_asset'),
    path('Insert_new_asset',views.Insert_Asset,name='insert_new_asset'),
    path('Edit_asset/<int:id>',views.Edit_Asset,name='Edit_Asset'),
    path('update_asset/<int:id>',views.Update_Asset,name='update_Asset'),
    path('asset_info/<int:id>',views.Asset_Info,name='Asset_info'),
    path('asset_del/<int:id>',views.Asset_Delete,name='Asset_delete'),

]

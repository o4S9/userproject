from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
import pandas as pd
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.template import loader


# user password Onkar$$$***000
# Create your views here.
def index(request):
#    print(request.user)
   if request.user.is_anonymous:
        # addl = request.POST.get('addl')  
        # contact = Barcode(addl)
        # contact.save()
        return redirect('/login') 
#    if request.method == 'POST':
#         addl = request.POST.get('addl')  
#         contact = Barcode(addl)
#         contact.save()
        
   return render(request, 'index.html') 

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        # check if user is logged
        user = authenticate(username=username, password=password) 
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/upload/')
            
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html') 
           
        
    return render(request, 'login.html') 

def logoutuser(request):
    logout(request)
    return redirect('/login') 

def view_data(request):
    if request.method == 'POST':
        barcode = request.POST.get('code')
        li = [barcode,]
        # print("List:",li)
        for i in li:
            print("List :",i) 
        # if barcode:
        #     print('Barcode',barcode)
        
        # loop = Barcode(barcode)
        # print('BARCODE :',barcode)
        # for i in barcode:
        #     print('Barcode',i)
            
            # Barcode.objects.get_or_create(code=barcode)
            # Barcode.save()   
    # data = YourModel.objects.all()
    # return render(request, 'view_data.html', {'data': data})
    # print(addl_input)
    # data = YourModel.objects.filter(addl=addl_input)
    # return render(request, 'view_data.html', {'data': data})
    # if addl_input:
    #     records = YourModel.objects.filter(addl=addl_input)
    # else:
    #     records = []
    records = dataEntry.objects.all()
    return render(request, 'view_data.html',{'records': records})

    # return render(request, 'view_data.html')
    

def ScannerSheet(request):
    if request.method == "POST":
        barcodeInput = request.POST.get('barcodeRead')
        # email = request.POST.get('email')
        # phone = request.POST.get('phone')
        # desc = request.POST.get('desc')
        print(barcodeInput)
        contact = Scannerinput(barcodeInput)
        contact.save()
    data = Scannerinput.objects.all()
    return render(request, 'Scanning_sheet.html', {'data': data})

    # return render(request,'Scanning_sheet.html')
@csrf_exempt
def save_barcode(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        id = request.GET.get('locationInput')  # or request.POST.get('addl') if form is POST

        print(id,barcode)
        
        # print(barcode)
        # contact = Barcode(barcode)
        # contact.save()
        # if id == "":
        #     return render(request, 'scanner.html')
        # else:
        #     if barcode:
        #         print(barcode,id)
                # Barcode.objects.get_or_create(id=id,code=barcode)   
                # records = Barcode.objects.all()
        
                # return JsonResponse({'success': True})
            # if id:
            #     Barcode.objects.get_or_create(id=id) 
            #     return render(request, 'scanner.html')
        # query = request.GET.get('addl', '')  # input name="search"
        # if query:
        #     records = YourModel.objects.filter(addl=query)
        # else:  
        #     records = YourModel.objects.all()

        # return render(request, 'scanner.html', {'records': records, 'query': query})
    # barcode = request.GET.get('barcode')  # or request.POST.get('addl') if form is POST
        # if barcode:
        #     print('ADDL =',barcode)
        #     records = YourModel.objects.filter(addl=barcode)
        #     return render(request, 'view_data.html', {'records': records})
    # return HttpResponse(template.render(context, request),) 
    # print(addl_input)
    # records = YourModel.objects.filter(addl=addl_input)
        # records = YourModel.objects.filter(addl='8275444939')
        # return render(request, 'scanner.html',{'records': records})

    
        # records = YourModel.objects.filter(addl='8275444939')
        # return render(request, 'scanner.html',{'records': records})
        # records = Barcode.objects.all()
        # return render(request, 'scanner.html',{'records': records})
    records = Barcode.objects.all()
    return render(request, 'scanner.html',{'records': records})
   
        # return render(request, 'scanner.html', {'data': data})
    # return render(request,'scanner.html',{'data': data})



def dataEntry(request):  
    # selected_code = None
    selected_product = None
    # product_name = ""
    # selected_code1 = None
    loc = location.objects.values_list('id', flat=True).distinct()

        # print(i)
    # if request.method == "POST":
    #     addl = request.POST.get('addl')
    #     selected_code1 = request.POST.get('loca')
    #     print("CODE 1:",selected_code1)
    #     print("CODE 1.5:",addl)

       
    if request.method == "POST":
        selected_code = request.POST.get('lno')
        print("CODE 2:",selected_code)
        
        selected_product = location.objects.filter(loc_vise=selected_code).first()
        return render(request,'Data_Entry.html',{'loc':loc,'selected_code':selected_product })

        # return render(request,'Data_Entry.html')

    if request.method == "POST":
        addl = request.POST.get('addl')
        selected_code1 = request.POST.get('loca')
        idnumber = request.POST.get('no')
        today =  datetime.today().date()
        print("CODE 1:",idnumber)
        # if addl == "":
        #     print("Please scan barcode")
        # else:
        #     loctionRecords.objects.create(my_date=today, loc_rec=idnumber, add_item_list=addl)
        #     return render(request,'Data_Entry.html',{"ln":idnumber})


        # print("CODE 1.5:",addl)
        # print("CODE 2:",idnumber)

        # loctionRecords.objects.create(my_date=today, loc_rec=selected_code1, add_item_list=addl)
        # addl = ''
        # selected_code1= ''
        # print('recors is empty!',addl,selected_code1)
        # print("Data Submited")
        # Sloc = location.objects.filter(loc_vise=selected_code1).first()
        # print("CODE 3:",Sloc)

        # if selected_product:
        #       product_name = location.loc_vise         
        # print("LOC AND ADDL :",loc)
    # numbers = list(range(1, 11))  # generates [1, 2, 3, ..., 500]
    # today =  datetime.today().date()
    # for i in range(1, 501):
    #     location.objects.create(my_date=today,loc_vise=str(i))
        # print("Data Submited")
    return render(request,'Data_Entry.html',{'loc':loc,'selected_code':selected_product })


def setlocation(request):
    selected_code = None
    selected_product = None
    loc = location.objects.values_list('id', flat=True).distinct()

    if request.method == "POST":
        selected_code = request.POST.get('lno')
        print("CODE 3:",selected_code)
        # selected_product = location.objects.filter(loc_vise=selected_code).first()
    #     # # selected_product = location.objects.filter(loc_vise=selected_code).first()
        # return render(request,'set_location.html',{'selected_code': selected_product})
    return render(request,'set_location.html',{'loc':loc})


def upload_form(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        item_code = request.POST.get('item_code')
        item_name = request.POST.get('item_name')
        

        if location != "":
            listloc = [location,]
            print("Location :",listloc)
            loc = YourModel.objects.filter(location = location).values()
            return render(request,"media.html",{"location": loc})
        elif item_code != "":
            print("Item_code :",item_code)
            loc = YourModel.objects.filter(itemcode = item_code).values()
            return render(request,"media.html",{"location": loc})
        elif item_name != "":
            print("Item_name :",item_name)
            loc = YourModel.objects.filter(itemname = item_name).values()
            return render(request,"media.html",{"location": loc})
        else:
            print("Please Enter any one option")
        # data =  YourModel.objects.all().values()
        # return render(request,"media.html",{'data':data})


    
    

    data =  YourModel.objects.all().values()
    return render(request,"media.html",{'data':data})


import pandas as pd
from django.conf import settings


# class ExportImportExcel():
#      def get(sel,request):
#          loc =    


# def post(self,request):
#     exceled_upload_obj = ExcelFileUpload.objects.create(excel_file_upload = request.FILES['files'])
#     df = pd.read_csv(f"{settings.BASE_DIR}/static/{exceled_upload_obj.excel_file_upload}")
#     print(df.values.tolist())
#     return HttpResponse({'status':200})



def create_bd(file_path):
    filePath = file_path
    df = pd.read_excel(filePath)
    # print(df.values)
    list_of_csv = [list(row) for row in df.values]
    for l in list_of_csv:
        YourModel.objects.create(
            location  = l[0],
            addl      = l[1],
            itemcode  = l[2],
            itemname  = l[3],
            size      = l[4],
            qty       = l[5],
        )

def main(request):
    if request.method == "POST":
        file = request.FILES['file'] 
        obj = File.objects.create(file = file)
        create_bd(obj.file)
    return render(request,'upload.html')

# create_bd("files\Andheri_SCANNING_SHEET_17-07-25_NqlRATL.xlsx") 
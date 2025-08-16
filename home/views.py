from urllib.parse import urlencode
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from django.urls import reverse
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
   addl = None
   itename = None
   if request.user.is_anonymous:
        # addl = request.POST.get('addl')  
        # contact = Barcode(addl)
        # contact.save()
        return redirect('/login') 
   MasterCount = MasterData.objects.exclude(ADDL = True).count()
   StockCount = StockData.objects.exclude(BARCODE = True).count()
   ScanningCount = loctionRecords.objects.exclude(add_item_list = True).count()
   if request.method == "POST":
       addl = request.POST.get("addl")
       itename = request.POST.get("itename")
   if addl:
       master = MasterData.objects.filter(ADDL = addl).values()
    #    print(master)
       return render(request,"index.html",{"masterProducts":master,"Count":MasterCount,"Scount":StockCount,"Sccount":ScanningCount,})
   elif itename:
       master = MasterData.objects.filter(ADDL = addl).values()
       return render(request,"index.html",{"masterProducts":master,"Count":MasterCount,"Scount":StockCount,"Sccount":ScanningCount,})
   return render(request, 'index.html',{
       "Count":MasterCount,
       "Scount":StockCount,
       "Sccount":ScanningCount,       
       }) 

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
            return redirect('/')
            
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html') 
           
        
    return render(request, 'login.html') 

def logoutuser(request):
    logout(request)
    return redirect('/view')


# def fileView():
#     fl = ["Master File :",file,]
#     filePath = fl
#     df = pd.read_excel(filePath)
#     print(df)
#     list_of_csv = [list(row) for row in df.values]

def view_data(request):
    if request.method == 'POST':
        barcode = request.POST.get('code')
        li = [barcode,]
        # print("List:",li)
        for i in li:
            pass
            # print("List :",i) 
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
    # records = dataEntry.objects.all()
    return render(request, 'view_data.html')

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

        # print(id,barcode)
        
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
    # loc = location.objects.values_list('id', flat=True).distinct()

        # print(i)
    # if request.method == "POST":
    #     addl = request.POST.get('addl')
    #     selected_code1 = request.POST.get('loca')
    #     print("CODE 1:",selected_code1)
    #     print("CODE 1.5:",addl)

       
    # if request.method == "POST":
    #     selected_code = request.POST.get('lno')
    #     print("CODE Location:",selected_code) 
    #     selected_product = location.objects.filter(loc_vise=selected_code).first()
    #     print("Loc_vise :",selected_product)
    #     return render(request,'Data_Entry.html',{'selected_product': selected_product} )


      
    if request.method == "POST":
        loc = request.POST.get("location")
        addl = request.POST.get("addl")
        # print("Loc & Addl: ",loc,addl)
        Selected_barcode = StockData.objects.filter(BARCODE=addl).first()
        Selected_barcode_Master = MasterData.objects.filter(ITEMCODE = addl).first()
        # print(Selected_barcode)
        if Selected_barcode:
            barcode = StockData(SCANNINGDATA = addl)
            barData = loctionRecords(loc_rec = loc,add_item_list = addl)
            barcode.save()
            barData.save()
            return redirect('/dataEnter')
        elif Selected_barcode_Master:
            ser = ExcessRecordScanning(loc_rec = loc,add_item_list = addl)
            ser.save()
            return redirect('/dataEnter')
        else:
            # print("Barecode Not Match!")
            messages.success(request, "This Product Not in your Stock...")
            return redirect('/dataEnter')

        

    return render(request,'Data_Entry.html')


# def locSet(request):
#     if request.method == "POST":
#         selected_code = request.POST.get('lno')
#         print("CODE Location:",selected_code)            
#         selected_product = location.objects.filter(loc_vise=selected_code).first()
#         print("CODE Location2:",selected_product)  
#         return redirect("/dataEnter")  
#     #   
#     return render(request,'Data_Entry.html')


def view(request):
    selected_code = None
    selected_product = None
    loc = location.objects.values_list('id', flat=True).distinct()

    if request.method == "POST":
        selected_code = request.POST.get('lno')
        # print("CODE 3:",selected_code)
        # selected_product = location.objects.filter(loc_vise=selected_code).first()
    #     # # selected_product = location.objects.filter(loc_vise=selected_code).first()
        # return render(request,'set_location.html',{'selected_code': selected_product})
    return render(request,'view.html',{'loc':loc})

from django.db.models import Count
def upload_form(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        item_code = request.POST.get('item_code')
        item_name = request.POST.get('item_name')
        

        if location != "":
            listloc = [location,]
            # print("Location :",listloc)
            loc = YourModel.objects.filter(location = location).values()
            return render(request,"media.html",{"location": loc})
        elif item_code != "":
            # print("Item_code :",item_code)
            loc = YourModel.objects.filter(itemcode = item_code).values()
            return render(request,"media.html",{"location": loc})
        elif item_name != "":
            # print("Item_name :",item_name)
            loc = YourModel.objects.filter(itemname = item_name).values()
            return render(request,"media.html",{"location": loc})
        else:
            # print("Please Enter any one option")
            loc =  YourModel.objects.all().values()
            # print(loc)
            return render(request,"media.html",{'data':loc})
       
            # loc = YourModel.objects.filter(itemcode = item_code).values()
            # return redirect("/",{"data": loc})
    return render(request,'media.html')


def uploadMasterform(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        item_code = request.POST.get('item_code')
        item_name = request.POST.get('item_name')
        

        if location != "":
            listloc = [location,]
            # print("Location :",listloc)
            loc = File.objects.filter(location = location).values()
            return render(request,"masterImport.html",{"location": loc})
        elif item_code != "":
            # print("Item_code :",item_code)
            loc = File.objects.filter(itemcode = item_code).values()
            return render(request,"masterImport.html",{"location": loc})
        elif item_name != "":
            # print("Item_name :",item_name)
            loc = File.objects.filter(itemname = item_name).values()
            return render(request,"masterImport.html",{"location": loc})
        else:
            print("Please Enter any one option")
        # data =  YourModel.objects.all().values()
        # return render(request,"media.html",{'data':data})
       
            # loc = YourModel.objects.filter(itemcode = item_code).values()
            # return redirect("/",{"data": loc})
    return render(request,'masterImport.html')


    
    

    # data =  YourModel.objects.all().values()
    # results = YourModel.objects.values('itemname').annotate(total_count=Count('itemname'))
    # for row in results:
    #     print(f"{row['itemname']} - {row['total_count']}")
    #     return redirect("/media",{'data':data})



    # return render(request,"media.html",{'data':data})


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
    # print(list_of_csv)
    for l in list_of_csv:
        # print(l[0])
        StockData.objects.create(      
            BRANCHCODE	                             = l[0],
            BRANCHNAME	                             = l[1],
            COMPANY	                                 = l[2],
            ARTICLENO	                             = l[3],
            ITEMNAME	                             = l[4],
            COLOURS	                                 = l[5],
            BARCODE	                                 = l[6],
            EANCODE	                                 = l[7],
            SIZE	                                 = l[8],
            SECTION	                                 = l[9],
            BRAND                                    = l[10],
            SEASON                                   = l[11],
            ITEM_DESC                                = l[12],
            GROUP5_GRP1	                             = l[13],
            GENDER	                                 = l[14],
            GST	                                     = l[15],
            CLOSINGSTOCK                             = l[16],
            COST	                                 = l[17],
            MRP	                                     = l[18],
            CLOSINGVALUECOST                         = l[19],
            CLOSINGVALUEMRP                          = l[20],
            GODOWNNAME	                             = l[21],
            ITEMNAME_SHADESHORTNAME_PACKGROUPNAME    = l[22]
        )

def main(request):
    if request.method == "POST":
        file = request.FILES['file'] 
        obj  = stockFile.objects.create(file = file)
        create_bd(obj.file)
    return render(request,'upload.html')



# create_bd("files\Andheri_SCANNING_SHEET_17-07-25_NqlRATL.xlsx") 

# def master(request):
#     if request.method == "POST":
#         file = request.FILES['file'] 
#         File.objects.create(file = file)
#         # create_bd(obj.file)
#     return render(request,'masterImport.html')

def createMaster_bd(file_path):
    filePath = file_path
    df = pd.read_excel(filePath)
    # print(df)
    list_of_csv = [list(row) for row in df.values]
    # today =  datetime.today().date()
    for l in list_of_csv:
        MasterData.objects.create(
        ADDL         = l[0],
        ITEMCODE	 = l[1],
        ITEMNAME	 = l[2],
        SIZE	     = l[3],
        MRP	         = l[4],
        BRANDNAME    = l[5],
        SECTION      = l[6],
        BASICRATE    = l[7], 
        SEASON       = l[8],
        COLOURS      = l[9], 
        )

def upload_master(request):
    if request.method == "POST":
        file = request.FILES['file'] 
        # fl = ["Master File :",file,]
        obj  = File.objects.create(file = file)
        createMaster_bd(obj.file)
        return redirect('/master')

        # obj  = File.objects.create(file = file)
        # createMaster_bd(obj.file)
    return render(request,'masterImport.html')


def home(request):
    return render(request,'home.html')

def MasterDataCount(request):
    # MasterCount = MasterData.objects.exclude(ADDL = True).count()
    # MasterCount = MasterData.objects.all()
    # print("Count :",MasterCount)
    return render(request,"index.html")

def scannerFile(request):
    if request.method == "POST":
        location = request.POST.get("location")
        addl = request.POST.get("addl")
        print("L&AL :",location,addl)

    return render(request,'Data_Entry.html')

# user view 
def userView(request):
    return render(request, "userView.html")
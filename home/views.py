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
from django.db.models import Count, OuterRef, Subquery,F,IntegerField


# user password Onkar$$$***000
# Create your views here.
def index(request):
#    print(request.user)
   addl = None
   itename = None
   if request.user.is_anonymous:
        return redirect('/login') 
   MasterCount = MasterData.objects.exclude(ADDL = True).count()
   StockCount = StockData.objects.exclude(BARCODE = True).aggregate(
    total=Sum('CLOSINGSTOCK') )['total']
   ScanningCount = loctionRecords.objects.exclude(add_item_list = True).count()
   ExcessCount = ExcessRecordScanning.objects.exclude(add_item_list = True).count()
#    print(MasteRec)
   if request.method == "POST":
       addl = request.POST.get("addl")
       itename = request.POST.get("itename")
   if addl:
       master = MasterData.objects.filter(ADDL = addl).values()
    #    print(master)
       return render(request,"index.html",{"masterProducts":master,"Count":MasterCount,"Scount":StockCount,"Sccount":ScanningCount,"Ecount":ExcessCount})
   elif itename:
       print(itename)
       master = MasterData.objects.filter(ITEMNAME = itename).values()
       return render(request,"index.html",{"masterProducts":master,"Count":MasterCount,"Scount":StockCount,"Sccount":ScanningCount,"Ecount":ExcessCount})

#    Short List Item

   return render(request, 'index.html',{
       "Count":MasterCount,
       "Scount":StockCount,
       "Sccount":ScanningCount,  
       "Ecount":ExcessCount     
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

    addl = None 
    loc  = None 
    lc   = None
    if request.method == "POST":
        loc  = request.POST.get("location")
        addl = request.POST.get("addl")
        lc   = request.POST.get("lc")
        cb   = request.POST.get('cb')
        ub   = request.POST.get('ub')
        # print(cb,ub)
        # print("Loc & Addl: ",loc,addl)
        Selected_barcode = StockData.objects.filter(EANCODE=addl).first()
        Selected_barcode_Master = MasterData.objects.filter(ADDL = addl).first()
        # print(Selected_barcode)
        displayBarcode = loctionRecords.objects.all().values()
        if addl == '':
            messages.success(request, "Please enter a barcode!")
        elif Selected_barcode:
            # barcode = StockData(scanningdata_id = addl)
            barData = loctionRecords(loc_rec = loc,add_item_list = addl)
            location_count = loctionRecords.objects.exclude(loc_rec = loc).count()
            dispaly = loctionRecords.objects.filter(loc_rec = loc).values()
            # barcode.save()
            barData.save()
            
            # print(displayBarcode)
            if Selected_barcode:
                location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c') 
                result = StockData.objects.values('EANCODE','BARCODE','ITEMNAME','SIZE','SECTION','MRP').annotate( home_stockdata=Count('EANCODE'), 
                home_loctionrecords=Subquery(location_count, output_field=models.IntegerField()) ).annotate( difference=F('home_loctionrecords') - F('home_stockdata') ) 
                # return render(request,'DBS&S.html',{"result":result})
            elif displayBarcode:
                # print(displayBarcode) 
                pass               
            return redirect('/dataEnter')

        elif Selected_barcode_Master:
            ser = ExcessRecordScanning(loc_rec = loc,add_item_list = addl)
            dispaly = loctionRecords.objects.filter(loc_rec = loc).values()
            ser.save()
            if Selected_barcode_Master:
                location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c') 
                result = StockData.objects.values('EANCODE','BARCODE','ITEMNAME','SIZE','SECTION','MRP').annotate( home_stockdata=Count('EANCODE'), 
                home_loctionrecords=Subquery(location_count, output_field=models.IntegerField()) ).annotate( difference=F('home_loctionrecords') - F('home_stockdata') ) 
                # return render(request,'DBS&S.html',{"result":result})
            return redirect('/dataEnter')
        elif lc:
            location_count = loctionRecords.objects.filter(loc_rec=lc).count() 
            dispaly = loctionRecords.objects.filter(loc_rec = lc).values()
            # print(dispaly)
            return render(request ,'Data_Entry.html',{"lCount":location_count,'display': dispaly})
        elif ub != "" and cb != "":
            # print(cb,ub)
            try:
                record = loctionRecords.objects.get( add_item_list=cb)
                record.add_item_list = ub
                record.save()
                # print(loc)
                # dispaly = loctionRecords.objects.filter(loc_rec = loc).values()
                msg = "✅ Barcode updated successfully!"
                messages.success(request, msg) 
                return render(request ,'Data_Entry.html')            

            except StockData.DoesNotExist:
                msg1 = "❌ Record not found!"
                messages.success(request, msg1)            

        else:
            # print("Barecode Not Match!")
            EBSc = ExcessScanning(loc_rec = loc,add_item_list = addl)
            EBSc.save()             
            messages.success(request, "This is a Invalid Barcode")            
            # mr = MasterData.objects.filter(ITEMCODE = dlr).values()
            # print("Scanning REc :",mr)
           
            location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c') 
            result = StockData.objects.values('EANCODE','BARCODE','ITEMNAME','SIZE','SECTION','MRP').annotate( home_stockdata=Count('EANCODE'), 
            home_loctionrecords=Subquery(location_count, output_field=models.IntegerField()) ).annotate( difference=F('home_loctionrecords') - F('home_stockdata') ) 
            
            return redirect('/dataEnter')

        # if request.method == 'POST':
        #     cb = request.POST.get('cb')
        #     ub = request.POST.get('ub')
        #     print(cb,ub)
    # location_count = loctionRecords.objects.filter(
    # add_item_list=OuterRef('BARCODE')
    # ).values('add_item_list').annotate(
    #     c=Count('id')
    # ).values('c')
    # result = StockData.objects.values('BARCODE').annotate(
    #     home_stockdata=Count('BARCODE'),
    #     home_loctionrecords=Subquery(location_count, output_field=models.IntegerField())
    # ).annotate(
    #     difference=F('home_loctionrecords') - F('home_stockdata')
    # )
    location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c') 
    result = StockData.objects.values('EANCODE','BARCODE','ITEMNAME','SIZE','SECTION','MRP').annotate( home_stockdata=Count('EANCODE'), 
    home_loctionrecords=Subquery(location_count, output_field=models.IntegerField()) ).annotate( difference=F('home_loctionrecords') - F('home_stockdata') ) 
    dispaly = loctionRecords.objects.filter(loc_rec = loc).values()
    # print(dispaly)
    return render(request,'Data_Entry.html',{'display': dispaly})


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

# def create_bdsc(file_path):
#     filePath = file_path
#     df = pd.read_excel(filePath)
#     # print(df)
#     list_of_csv = [list(row) for row in df.values]
#     # today =  datetime.today().date()
#     # list_of_csv = [list(row) for row in df.values]
#     # print(list_of_csv)
#     # for l in list_of_csv:
#     #     print(l)
#         # loctionRecords.objects.create(      
#         #     BRANCHCODE	                             = l[0],
        
#         # )
# def scan(request):
#     if request.method == "POST":
#         file = request.FILES['file'] 
#         obj  = scanningFile.objects.create(file = file)
#         # print(obj)
#         create_bdsc(obj.file)
#         return redirect("/scan")
#     return render(request,'importScanningFIle.html')

def createScan_bd(file_path):
    filePath = file_path
    df = pd.read_excel(filePath)
    # print(df)
    list_of_csv = [list(row) for row in df.values]
    # today =  datetime.today().date()
    for l in list_of_csv:
        loctionRecords.objects.create(
        loc_rec         = l[0],
        add_item_list = l[1],
        )

def upload_scanning(request):
    if request.method == "POST":
        file = request.FILES['file'] 
        # fl = ["Master File :",file,]
        obj  = scanningFile.objects.create(file = file)
        createScan_bd(obj.file)
       
        return redirect('/scan')
     
      
    scanRec = loctionRecords.objects.all()
    return render(request,'importScanningFIle.html',{'display':scanRec})
def downloadScan(request):
    scanRec = loctionRecords.objects.all()
    if request.method == "POST":
        download = request.POST.get('download') 
        # print(download)
        if download == "":
            data = list(scanRec)   # result is your queryset with annotate()
            # Load into Pandas
            df = pd.DataFrame(data)
            # print(df)
            # Specify download path (example for Windows)
            download_path = r"C:/Users/Onkar/Downloads/StockVScanningData.xlsx"
            # # Make sure directory exists
            os.makedirs(os.path.dirname(download_path), exist_ok=True)
            # # Save to Excel
            df.to_excel(download_path, index=False)
    
    return render(request,'downloadScanningData.html',{'display':scanRec})

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
import os
from django.db.models.functions import Coalesce
from django.db.models import OuterRef, Subquery, Count, F, IntegerField, Value,Sum,ExpressionWrapper
def differencSS(request):
    status = None
    location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c') 
        # Step 1 → Aggregate sum of stock, explicitly as Integer
    qs = StockData.objects.values(
        'EANCODE', 'BARCODE', 'ITEMNAME', 'SIZE', 'BRAND','SECTION', 'MRP'
    ).annotate(
        stock_sum=Sum('CLOSINGSTOCK', output_field=IntegerField()),   # force numeric
        home_loctionrecords=Subquery(location_count, output_field=IntegerField())
    )

    # Step 2 → Wrap with Coalesce and compute difference safely
    result = qs.annotate(
        home_stockdata=Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
        home_loctionrecords=Coalesce(F('home_loctionrecords'), Value(0), output_field=IntegerField()),
        difference=ExpressionWrapper(
            F('home_loctionrecords') - Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
            output_field=IntegerField()  # enforce integer output
        )
    )
   
    # RESULT1
    result1 = qs.annotate(
        home_stockdata=Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
        home_loctionrecords=Coalesce(F('home_loctionrecords'), Value(0), output_field=IntegerField()),
        difference=ExpressionWrapper(
            F('home_loctionrecords') - Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
            output_field=IntegerField()  # enforce integer output
        )
    ).filter(difference__lt=0)  # 👈 correct way 
    result2 = qs.annotate(
    home_stockdata=Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
    home_loctionrecords=Coalesce(F('home_loctionrecords'), Value(0), output_field=IntegerField()),
    difference=ExpressionWrapper(
        F('home_loctionrecords') - Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
        output_field=IntegerField()  # enforce integer output
    )
    ).filter(difference__gt=0)  # 👈 correct way 
    # df = pd.DataFrame(list(result))
    # print(result)
    if request.method == 'POST':
        status = request.POST.get('status')
        download = request.POST.get('download')
        # print(download)
        if status == 'all':
            return render(request,'DBS&S.html',{"result":result,})
        elif status == 'short':
            return render(request,'DBS&S.html',{"result":result1,})
        elif status == 'excess':
            return render(request,'DBS&S.html',{"result":result2,})
        elif download == 'download':
            data = list(result)   # result is your queryset with annotate()
            # Load into Pandas
            df = pd.DataFrame(data)
            # Specify download path (example for Windows)
            download_path = r"C:/Users/Onkar/Downloads/StockVScanningDiffData.xlsx"
            # Make sure directory exists
            os.makedirs(os.path.dirname(download_path), exist_ok=True)
            # Save to Excel
            df.to_excel(download_path, index=False)
            # print(f"File saved to: {download_path}")
            return redirect('/ss')
        else:
            pass
            # print(status)

  


    return render(request,'DBS&S.html')

def short(request):
    location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c') 
    qs = StockData.objects.values(
        'EANCODE', 'BARCODE', 'ITEMNAME', 'SIZE', 'BRAND','SECTION', 'MRP'
    ).annotate(
        stock_sum=Sum('CLOSINGSTOCK', output_field=IntegerField()),   # force numeric
        home_loctionrecords=Subquery(location_count, output_field=IntegerField())
    )
 # RESULT1
    result1 = qs.annotate(
        home_stockdata=Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
        home_loctionrecords=Coalesce(F('home_loctionrecords'), Value(0), output_field=IntegerField()),
        difference=ExpressionWrapper(
            F('home_loctionrecords') - Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
            output_field=IntegerField()  # enforce integer output
        )
    ).filter(difference__lt=0)  # 👈 correct way  
     
    
    return render(request, "shortFile.html",{"result":result1,}) 

def excess(request):
    location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c') 
    qs = StockData.objects.values(
        'EANCODE', 'BARCODE', 'ITEMNAME', 'SIZE', 'BRAND','SECTION', 'MRP'
    ).annotate(
        stock_sum=Sum('CLOSINGSTOCK', output_field=IntegerField()),   # force numeric
        home_loctionrecords=Subquery(location_count, output_field=IntegerField())
    )
    result2 = qs.annotate(
    home_stockdata=Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
    home_loctionrecords=Coalesce(F('home_loctionrecords'), Value(0), output_field=IntegerField()),
    difference=ExpressionWrapper(
        F('home_loctionrecords') - Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
        output_field=IntegerField()  # enforce integer output
    )
    ).filter(difference__gt=0)  # 👈 correct way 
    # res = StockData.objects.values('BARCODE','ITEMNAME','SIZE','SECTION','MRP')
    # df = pd.DataFrame(list(res))
    # print(df)

    
    return render(request, "excess.html",{"result":result2,}) 
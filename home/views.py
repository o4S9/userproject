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
   StockCount = StockData.objects.exclude(EANCODE = True).count() #aggregate(total=Sum('CLOSINGSTOCK') )['total']
   ScanningCount = loctionRecords.objects.exclude(add_item_list = True).count()
   ExcessCount = ExcessRecordScanning.objects.exclude(add_item_list = True).count()
   nill = ExcessScanning.objects.exclude(add_item_list = True).count()
   difference = ScanningCount - StockCount
   differences = StockCount - ScanningCount
#    print(MasteRec)
   if request.method == "POST":
       addl = request.POST.get("addl")
       itename = request.POST.get("itename")
   if addl:
       master = MasterData.objects.filter(ADDL = addl).values()
    #    print(master)
       return render(request,"index.html",{"masterProducts":master,"Count":MasterCount,"Scount":StockCount,"Sccount":ScanningCount,"Ecount":ExcessCount,"nill":nill})
   elif itename:
       print(itename)
       master = MasterData.objects.filter(ITEMNAME = itename).values()
       return render(request,"index.html",{"masterProducts":master,"Count":MasterCount,"Scount":StockCount,"Sccount":ScanningCount,"Ecount":ExcessCount,"nill":nill})

#    Short List Item

   return render(request, 'index.html',{
       "Count":MasterCount,
       "Scount":StockCount,
       "Sccount":ScanningCount,
       "Ecount":ExcessCount,
       "nill":nill,
       'difference' : difference,
       'differences':differences
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
        inputaddl = request.POST.get("inputAddl")
        lc   = request.POST.get("lc")
        checkBox = request.POST.get('selected_items')
        # print(checkBox)
        # cl = list[checkBox]
        # for i in cl:
        #     print(i)
        # print('Update:',cb,ub)
        print("Loc & Addl: ",loc,addl,inputaddl)
        Selected_barcode = StockData.objects.filter(EANCODE=addl).first()
        Selected_barcode_Master = MasterData.objects.filter(ADDL = addl).first()
        # print('Addl 1:',addl, loc)
        displayBarcode = loctionRecords.objects.all().values()
        locationno = loctionRecords.objects.filter(loc_rec = loc).first()

        if Selected_barcode:
            # barcode = StockData(scanningdata_id = addl)
            barData = loctionRecords(loc_rec = loc,add_item_list = addl)
            location_count = loctionRecords.objects.exclude(loc_rec = loc).count()
            dispaly = loctionRecords.objects.filter(loc_rec = loc).values()
            # barcode.save()
            barData.save()
            # print(displayBarcode)
            if Selected_barcode:
                # Match loctionRecords.add_item_list with MasterData.ADDL
                master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
                result =loctionRecords.objects.annotate(
                        ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
                        ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
                        SIZE=Subquery(master_qs.values('SIZE')[:1]),
                        MRP=Subquery(master_qs.values('MRP')[:1]),
                        BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
                        SECTION=Subquery(master_qs.values('SECTION')[:1]),
                        SEASON=Subquery(master_qs.values('SEASON')[:1]),
                        COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
                        ).values(
                            'id', 'add_item_list', 'loc_rec','ITEMCODE',
                            'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                            'SECTION', 'SEASON', 'COLOURS'
                        )
                # return redirect('/dataEnter')
                # print(result)

            # return redirect('/dataEnter')

        elif Selected_barcode_Master:
            ser = ExcessRecordScanning(loc_rec = loc,add_item_list = addl)
            dispaly = loctionRecords.objects.filter(loc_rec = loc).values()
            ser.save()
            if Selected_barcode_Master:
                # loc_vise_excess_Rec = loctionRecords(loc_rec = loc,add_item_list = addl)
                # loc_vise_excess_Rec.save()
                master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
                result = loctionRecords.objects.annotate(
                            ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
                            ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
                            SIZE=Subquery(master_qs.values('SIZE')[:1]),
                            MRP=Subquery(master_qs.values('MRP')[:1]),
                            BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
                            SECTION=Subquery(master_qs.values('SECTION')[:1]),
                            SEASON=Subquery(master_qs.values('SEASON')[:1]),
                            COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
                            ).values(
                                'id', 'add_item_list', 'loc_rec','ITEMCODE',
                                'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                                'SECTION', 'SEASON', 'COLOURS'
                            )
                # return render(request,'Data_Entry.html',{"result":result})
            # return redirect('/dataEnter')
        
        elif lc:
            location_count = loctionRecords.objects.filter(loc_rec=lc).count()
            # Match loctionRecords.add_item_list with MasterData.ADDL
            master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
            result =loctionRecords.objects.filter(loc_rec=lc).annotate(
                        ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
                        ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
                        SIZE=Subquery(master_qs.values('SIZE')[:1]),
                        MRP=Subquery(master_qs.values('MRP')[:1]),
                        BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
                        SECTION=Subquery(master_qs.values('SECTION')[:1]),
                        SEASON=Subquery(master_qs.values('SEASON')[:1]),
                        COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
                        ).values(
                            'id', 'add_item_list', 'loc_rec','ITEMCODE',
                            'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                            'SECTION', 'SEASON', 'COLOURS'
                        )
            # print(result)
            return render(request,'Data_Entry.html',{"result":result,"lCount":location_count})

        elif checkBox:
            # print('ChecBox :',checkBox)
            product = loctionRecords.objects.get(id=checkBox)  # find row with id=1
            product.delete()
            master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
            result = loctionRecords.objects.annotate(
                    ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
                    ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
                    SIZE=Subquery(master_qs.values('SIZE')[:1]),
                    MRP=Subquery(master_qs.values('MRP')[:1]),
                    BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
                    SECTION=Subquery(master_qs.values('SECTION')[:1]),
                    SEASON=Subquery(master_qs.values('SEASON')[:1]),
                    COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
                    ).values(
                        'id', 'add_item_list', 'loc_rec','ITEMCODE',
                        'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                        'SECTION', 'SEASON', 'COLOURS'
                    )
            msg1 = "Record delete!"
            messages.success(request, msg1)

        #     return render(request,'Data_Entry.html',{"result":result})
                # return redirect('/dataEnter')
        # except loctionRecords.DoesNotExist:
        #
        
        else:
            
            if inputaddl:
                EBSc = ExcessScanning(loc_rec = loc,add_item_list = addl)
                EBSc.save()
                messages.error(request, "❌ This is an Invalid Barcode")            # mr = MasterData.objects.filter(ITEMCODE = dlr).values()
                return redirect('/dataEnter')
            # print("Scanning REc :",mr)
            master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
            result =loctionRecords.objects.filter(loc_rec=loc).annotate(
            ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
            ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
            SIZE=Subquery(master_qs.values('SIZE')[:1]),
            MRP=Subquery(master_qs.values('MRP')[:1]),
            BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
            SECTION=Subquery(master_qs.values('SECTION')[:1]),
            SEASON=Subquery(master_qs.values('SEASON')[:1]),
            COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
            ).values(
                'id', 'add_item_list', 'loc_rec','ITEMCODE',
                'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                'SECTION', 'SEASON', 'COLOURS'
            )

            return render(request,'Data_Entry.html',{"result":result})
     


    


    if request.method == "GET":
        locationNo = request.GET.get("locationNo")
        Addl = request.GET.get("ITEMNAME")
        locn = loctionRecords.objects.filter(loc_rec = locationNo).values()
        addl = StockData.objects.filter(EANCODE = Addl).values()
        # print("itename0 :",itename,locn)
        # return redirect('/dataEnter')

        if addl:            
            master_qs = StockData.objects.filter(EANCODE=addl)
            result =loctionRecords.objects.annotate(
                    ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
                    ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
                    SIZE=Subquery(master_qs.values('SIZE')[:1]),
                    MRP=Subquery(master_qs.values('MRP')[:1]),
                    BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
                    SECTION=Subquery(master_qs.values('SECTION')[:1]),
                    SEASON=Subquery(master_qs.values('SEASON')[:1]),
                    COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
                    ).values(
                        'id', 'add_item_list', 'loc_rec','ITEMCODE',
                        'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                        'SECTION', 'SEASON', 'COLOURS'
                    )
            # return redirect('/dataEnter')
            # print(result)
            return render(request,'Data_Entry.html',{"result":result})
            
        elif locn:
            # print("itename3 :",locn)
            delete = loctionRecords.objects.filter(loc_rec=locationNo)
            delete.delete() 
            msg1 = "❌ Records Deleted!"
            messages.success(request, msg1)
            return redirect('/dataEnter')
        
   
    master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
    result =loctionRecords.objects.filter(loc_rec=loc).annotate(
            ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
            ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
            SIZE=Subquery(master_qs.values('SIZE')[:1]),
            MRP=Subquery(master_qs.values('MRP')[:1]),
            BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
            SECTION=Subquery(master_qs.values('SECTION')[:1]),
            SEASON=Subquery(master_qs.values('SEASON')[:1]),
            COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
            ).values(
                'id', 'add_item_list', 'loc_rec','ITEMCODE',
                'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                'SECTION', 'SEASON', 'COLOURS'
            )
    return render(request,'Data_Entry.html',{"result":result})



def updateAddl(request):
    if request.method == 'POST':
        cb = request.POST.get('cb')
        ub = request.POST.get('ub')
        print(cb,ub)
    return redirect('/dataEnter')


def view(request):
    selected_code = None
    selected_product = None
    loc = location.objects.values_list('id', flat=True).distinct()

    if request.method == "POST":
        selected_code = request.POST.get('lno')

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
            pass
            # print("Please Enter any one option")
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
        delfile = request.POST.get("filename")

        if file == '':
            return redirect('/upload/')
        elif file != '':
            obj  = stockFile.objects.create(file = file)
            create_bd(obj.file)
            return redirect('/upload/')

    if request.method == "GET":
        deleteStock = request.GET.get("status")
        if deleteStock == "Stock":
            StockData.objects.all().delete()
            messages.success(request, "All records deleted successfully ✅")
            return redirect('/upload/')

    filerecord = stockFile.objects.all()
    return render(request,'upload.html',{'filerecord':filerecord})

def deleteStockFile(request):
    # if request.method == "POST":
    #     delfile = request.POST.get("filename")

    #     return redirect('/upload/')
    obj = StockData.objects.all().delete()
    obj.delete()
    return render(request,'short.html')



@csrf_exempt
def update_barcode(request):
    if request.method == 'POST':
        location = request.POST.get('locationNo')
        addl = request.POST.get('addl')
        update_addl = request.POST.get('updateAddl')
        # record = loctionRecords.objects.get( add_item_list=addl)
        # record.add_item_list = update_addl
        # record.save()
        try:
            barcode = loctionRecords.objects.get(loc_rec=location, add_item_list=addl)
            barcode.addl = update_addl
            barcode.save()
            msg = "❌ Record not found!"
            messages.success(request, msg)
            # # print("Updated successfully.")
            return redirect("/dataEnter")
        except loctionRecords.DoesNotExist:
            msg = "❌ Record not found!"
            messages.success(request, msg)
            # print("Barcode entry not found.")
            return redirect("/dataEnter")
    return redirect("/dataEnter")

@csrf_exempt
def delete_barcode(request):
    if request.method == 'POST':
        location = request.POST.get('locationNo')
        addl = request.POST.get('addl')
        # Perform delete logic here
        return redirect('/scan')


def createScan_bd(file_path):
    filePath = file_path
    df = pd.read_excel(filePath)
    # print(df)
    list_of_csv = [list(row) for row in df.values]
    # today =  datetime.today().date()
    for l in list_of_csv:
        loc = l[0]
        addl = l[1]
        # print(addl)
        Selected_barcode = StockData.objects.filter(EANCODE=addl).first()
        Selected_barcode_Master = MasterData.objects.filter(ADDL = addl).first()
        # print(Selected_barcode)

        if addl == '':
            # print( "Please enter a barcode!")
            return redirect('/scan')
        elif Selected_barcode:
            # print(l)
            # barcode = StockData(scanningdata_id = addl)
            barData = loctionRecords(loc_rec = loc,add_item_list = addl)
            barData.save()
        elif Selected_barcode_Master:
            # print("Excess !")
            ser = ExcessRecordScanning(loc_rec = loc,add_item_list = addl)
            ser.save()
        else:
            # print("Not in Your Stock")
            EBSc = ExcessScanning(loc_rec = loc,add_item_list = addl)
            EBSc.save()

        # loctionRecords.objects.create(
        # loc_rec         = l[0],
        # add_item_list = l[1],
        # )

def upload_scanning(request):
    if request.method == "POST":
        file = request.FILES['file']
        # fl = ["Master File :",file,]
        obj  = scanningFile.objects.create(file = file)
        createScan_bd(obj.file)
        # return redirect('/scan')

    master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
    result = loctionRecords.objects.annotate(
                ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
                ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
                SIZE=Subquery(master_qs.values('SIZE')[:1]),
                MRP=Subquery(master_qs.values('MRP')[:1]),
                BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
                SECTION=Subquery(master_qs.values('SECTION')[:1]),
                SEASON=Subquery(master_qs.values('SEASON')[:1]),
                COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
                ).values(
                    'id', 'add_item_list', 'loc_rec','ITEMCODE',
                    'ITEMNAME', 'SIZE', 'MRP', 'BRANDNAME',
                    'SECTION', 'SEASON', 'COLOURS'
                )
    master_qs2 = MasterData.objects.filter(ADDL=OuterRef('add_item_list'))
    result2 = ExcessRecordScanning.objects.annotate(
                ITEMCODE=Subquery(master_qs2.values('ITEMCODE')[:1]),
                ITEMNAME=Subquery(master_qs2.values('ITEMNAME')[:1]),
                SIZE=Subquery(master_qs2.values('SIZE')[:1]),
                MRP=Subquery(master_qs2.values('MRP')[:1]),
                BRANDNAME=Subquery(master_qs2.values('BRANDNAME')[:1]),
                SECTION=Subquery(master_qs2.values('SECTION')[:1]),
                BASICRATE=Subquery(master_qs2.values('BASICRATE')[:1]),
                SEASON=Subquery(master_qs2.values('SEASON')[:1]),
                COLOURS=Subquery(master_qs2.values('COLOURS')[:1]),
            ).values(
               'id', 'add_item_list','loc_rec', 'ITEMCODE', 'ITEMNAME', 'SIZE',
                'MRP', 'BRANDNAME', 'SECTION', 'SEASON', 'COLOURS'
            )

    master_qs1 = MasterData.objects.filter(ADDL=OuterRef('add_item_list'))
    result1 = ExcessScanning.objects.annotate(
                ITEMCODE=Subquery(master_qs1.values('ITEMCODE')[:1]),
                ITEMNAME=Subquery(master_qs1.values('ITEMNAME')[:1]),
                SIZE=Subquery(master_qs1.values('SIZE')[:1]),
                MRP=Subquery(master_qs1.values('MRP')[:1]),
                BRANDNAME=Subquery(master_qs1.values('BRANDNAME')[:1]),
                SECTION=Subquery(master_qs1.values('SECTION')[:1]),
                BASICRATE=Subquery(master_qs1.values('BASICRATE')[:1]),
                SEASON=Subquery(master_qs1.values('SEASON')[:1]),
                COLOURS=Subquery(master_qs1.values('COLOURS')[:1]),
            ).values(
               'id', 'add_item_list','loc_rec', 'ITEMCODE', 'ITEMNAME', 'SIZE',
                'MRP', 'BRANDNAME', 'SECTION', 'SEASON', 'COLOURS'
            )
    if request.method == 'GET':
        status = request.GET.get('status')
        # delete = request.GET.get('selected_items')

        # print('Status :',status)
        # print('delete :',delete)

        if status == 'Scanning':
            # print('Scac :',status)
            return render(request,'importScanningFIle.html',{'display':result})
        elif status == 'Excess':
            # print('Exc :',status)
            return render(request,'importScanningFIle.html',{'display1':result2})
        elif status == 'Nill':
            # print('Nil :',status)
            return render(request,'importScanningFIle.html',{'display2':result1})
        else:
            pass
    if request.method == "GET":
        Sdelete = request.GET.get('selected_items')
        Edelete = request.GET.get('selected_itemsE')
        Ndelete = request.GET.get('selected_itemsN')
        
        if Sdelete:
            product = loctionRecords.objects.get(id=Sdelete)  # find row with id=1
            product.delete()
            msg1 = "Record delete!"
            messages.success(request, msg1)
            return render(request,'importScanningFIle.html',{"display":result})
        elif Edelete:
            # print(Edelete)
            product = ExcessRecordScanning.objects.get(id=Edelete)  # find row with id=1
            product.delete()
            msg1 = "Record delete!"
            messages.success(request, msg1)
            return render(request,'importScanningFIle.html',{"display1":result2})
        elif Ndelete:
            # print(Ndelete)
            product = ExcessScanning.objects.get(id=Ndelete)  # find row with id=1
            product.delete()
            msg1 = "Record delete!"
            messages.success(request, msg1)
            return render(request,'importScanningFIle.html',{"display2":result2})
    return render(request,'importScanningFIle.html',{
        'display':result,
        'display1':result2,
        'display2':result1
        })
    # scanRec = loctionRecords.objects.all()
    # excessRec = ExcessScanning.objects.all()
    # return render(request,'importScanningFIle.html',{'display':scanRec,'edisplay':excessRec})



from .models import MasterData,loctionRecords,ExcessRecordScanning,ExcessScanning
def downloadScan(request):
    # scanRec = loctionRecords.objects.all().values()
    # lis = list(scanRec)
    # print(lis)
    master_qs = StockData.objects.filter(EANCODE=OuterRef('add_item_list'))
    result = loctionRecords.objects.annotate(
                ITEMCODE=Subquery(master_qs.values('EANCODE')[:1]),
                ITEMNAME=Subquery(master_qs.values('ITEMNAME')[:1]),
                SIZE=Subquery(master_qs.values('SIZE')[:1]),
                MRP=Subquery(master_qs.values('MRP')[:1]),
                BRANDNAME=Subquery(master_qs.values('BRAND')[:1]),
                SECTION=Subquery(master_qs.values('SECTION')[:1]),
                SEASON=Subquery(master_qs.values('SEASON')[:1]),
                COLOURS=Subquery(master_qs.values('COLOURS')[:1]),
            ).values(
              'id', 'loc_rec','add_item_list','ITEMCODE', 'ITEMNAME', 'SIZE',
                'MRP', 'BRANDNAME', 'SECTION', 'SEASON', 'COLOURS'
            )
    master_qs2 = MasterData.objects.filter(ADDL=OuterRef('add_item_list'))
    result2 =ExcessRecordScanning.objects.annotate(
            ITEMCODE=Subquery(master_qs2.values('ITEMCODE')[:1]),
            ITEMNAME=Subquery(master_qs2.values('ITEMNAME')[:1]),
            SIZE=Subquery(master_qs2.values('SIZE')[:1]),
            MRP=Subquery(master_qs2.values('MRP')[:1]),
            BRANDNAME=Subquery(master_qs2.values('BRANDNAME')[:1]),
            SECTION=Subquery(master_qs2.values('SECTION')[:1]),
            BASICRATE=Subquery(master_qs2.values('BASICRATE')[:1]),
            SEASON=Subquery(master_qs2.values('SEASON')[:1]),
            COLOURS=Subquery(master_qs2.values('COLOURS')[:1]),
            ).values(
                'id','loc_rec','add_item_list','ITEMCODE', 'ITEMNAME', 'SIZE',
                'MRP', 'BRANDNAME', 'SECTION', 'SEASON', 'COLOURS'
            )
    master_qs1 = MasterData.objects.filter(ADDL=OuterRef('add_item_list'))
    result1 = ExcessScanning.objects.annotate(
                ITEMCODE=Subquery(master_qs1.values('ITEMCODE')[:1]),
                ITEMNAME=Subquery(master_qs1.values('ITEMNAME')[:1]),
                SIZE=Subquery(master_qs1.values('SIZE')[:1]),
                MRP=Subquery(master_qs1.values('MRP')[:1]),
                BRANDNAME=Subquery(master_qs1.values('BRANDNAME')[:1]),
                SECTION=Subquery(master_qs1.values('SECTION')[:1]),
                BASICRATE=Subquery(master_qs1.values('BASICRATE')[:1]),
                SEASON=Subquery(master_qs1.values('SEASON')[:1]),
                COLOURS=Subquery(master_qs1.values('COLOURS')[:1]),
            ).values(
                'id','loc_rec','add_item_list','ITEMCODE', 'ITEMNAME', 'SIZE',
                'MRP', 'BRANDNAME', 'SECTION', 'SEASON', 'COLOURS'
            )

    if request.method == 'POST':
        status = request.POST.get('status')

        if status == 'Scanning':
            return render(request,'downloadScanningData.html',{'display':result})
        elif status == 'Excess':
            return render(request,'downloadScanningData.html',{'display':result2})
        elif status == 'Nill':
            return render(request,'downloadScanningData.html',{'display':result1})
        else:
            pass
            # print(status)

    if request.method == "POST":
        Download = request.POST.get('download')
        print('status :',Download)
        if Download == "Scanning":
            # print(download)
            if Download == "Scanning":
                # print(download)
                data = list(result)   # result is your queryset with annotate()
                # data = list(result)   # result is your queryset with annotate()
                # Create DataFrame
                df = pd.DataFrame(data)
                # Load into Pandas DataFrame
                excel_buffer = BytesIO()

                # Use ExcelWriter and specify a sheet name
                with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    # Ensure at least one visible sheet is written
                    if not df.empty:
                        df.to_excel(writer, index=False, sheet_name='Data')
                    else:
                        # Create an empty sheet with headers only
                        pd.DataFrame(columns=["name", "price"]).to_excel(writer, index=False, sheet_name='Data')

                # Seek to the beginning of the BytesIO buffer
                excel_buffer.seek(0)

                # Create the HTTP response
                response = HttpResponse(
                    excel_buffer.getvalue(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=ScanningData.xlsx'

                return response
            return render(request,'downloadScanningData.html',{'display':result})

        elif Download == "Excess":
            # print(download)
            if Download == "Excess":
                data = list(result2)   # result is your queryset with annotate()
                            # data = list(result)   # result is your queryset with annotate()
                  # Create DataFrame
                df = pd.DataFrame(data)
                # Load into Pandas DataFrame
                excel_buffer = BytesIO()

                # Use ExcelWriter and specify a sheet name
                with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    # Ensure at least one visible sheet is written
                    if not df.empty:
                        df.to_excel(writer, index=False, sheet_name='Data')
                    else:
                        # Create an empty sheet with headers only
                        pd.DataFrame(columns=["name", "price"]).to_excel(writer, index=False, sheet_name='Data')

                # Seek to the beginning of the BytesIO buffer
                excel_buffer.seek(0)

                # Create the HTTP response
                response = HttpResponse(
                    excel_buffer.getvalue(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=ExcessScanningData.xlsx'

                return response
            return render(request,'downloadScanningData.html',{'display':result2})

        elif Download == "Nill":
            # print(download)
            if Download == "Nill":
                data = list(result1)   # result is your queryset with annotate()
                            # data = list(result)   # result is your queryset with annotate()
                  # Create DataFrame
                df = pd.DataFrame(data)
                # Load into Pandas DataFrame
                excel_buffer = BytesIO()

                # Use ExcelWriter and specify a sheet name
                with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    # Ensure at least one visible sheet is written
                    if not df.empty:
                        df.to_excel(writer, index=False, sheet_name='Data')
                    else:
                        # Create an empty sheet with headers only
                        pd.DataFrame(columns=["name", "price"]).to_excel(writer, index=False, sheet_name='Data')

                # Seek to the beginning of the BytesIO buffer
                excel_buffer.seek(0)

                # Create the HTTP response
                response = HttpResponse(
                    excel_buffer.getvalue(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=NillScanningData.xlsx'

                return response
            return render(request,'downloadScanningData.html',{'display':result1})
    if request.method == 'GET':
        deleteRec = request.GET.get('status')

        # print(ln,addl)
        if deleteRec == "Scanning":
            loctionRecords.objects.all().delete()
            messages.success(request, "All records deleted successfully ✅")
            return redirect("/scand")
        elif deleteRec == "Excess":
            ExcessRecordScanning.objects.all().delete()
            messages.success(request, "All records deleted successfully ✅")
            return redirect("/scand")
        elif deleteRec == "Nill":
            ExcessScanning.objects.all().delete()
            messages.success(request, "All records deleted successfully ✅")
            return redirect("/scand")

    return render(request,'downloadScanningData.html',{'display':result})

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
    return redirect('/master')

def upload_master(request):
    if request.method == "POST":
        file = request.FILES['file']
        # fl = ["Master File :",file,]
        obj  = File.objects.create(file = file)
        createMaster_bd(obj.file)
        return redirect('/master')
    if request.method == "GET":
        deleteStock = request.GET.get("status")
        if deleteStock == "Master":
            MasterData.objects.all().delete()
            messages.success(request, "All records deleted successfully ✅")
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
from django.db.models import OuterRef, Subquery, Count, F, IntegerField, Value,Sum,ExpressionWrapper,Exists
from io import BytesIO

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
        # download = request.POST.get('download')
        # print("Dowmload :",download)
        if status == 'all':
            return render(request,'DBS&S.html',{"result":result,})
        elif status == 'short':
            return render(request,'DBS&S.html',{"result":result1,})
        elif status == 'excess':

            return render(request,'DBS&S.html',{"result":result2,})



        else:
            pass
            # print(status)


    if request.method == 'POST':
        download = request.POST.get('download')
        # print("Dowmload :",download)
        if download == 'all':
            data = list(result)   # result is your queryset with annotate()
              # Create DataFrame
            df = pd.DataFrame(data)
            # Load into Pandas DataFrame
            excel_buffer = BytesIO()

            # Use ExcelWriter and specify a sheet name
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                # Ensure at least one visible sheet is written
                if not df.empty:
                    df.to_excel(writer, index=False, sheet_name='Data')
                else:
                    # Create an empty sheet with headers only
                    pd.DataFrame(columns=["name", "price"]).to_excel(writer, index=False, sheet_name='Data')

            # Seek to the beginning of the BytesIO buffer
            excel_buffer.seek(0)

            # Create the HTTP response
            response = HttpResponse(
                excel_buffer.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; filename=StockVScanningDiffAllData.xlsx'

            return response

        elif download == 'short':
            # print(download)
            data = list(result1)   # result is your queryset with annotate()
              # Create DataFrame
            df = pd.DataFrame(data)
            # Load into Pandas DataFrame
            excel_buffer = BytesIO()

            # Use ExcelWriter and specify a sheet name
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                # Ensure at least one visible sheet is written
                if not df.empty:
                    df.to_excel(writer, index=False, sheet_name='Data')
                else:
                    # Create an empty sheet with headers only
                    pd.DataFrame(columns=["name", "price"]).to_excel(writer, index=False, sheet_name='Data')

            # Seek to the beginning of the BytesIO buffer
            excel_buffer.seek(0)

            # Create the HTTP response
            response = HttpResponse(
                excel_buffer.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; filename=StockVScanningDiffShortData.xlsx'

            return response

        elif download == 'excess':
            data = list(result2)   # result is your queryset with annotate()
              # Create DataFrame
            df = pd.DataFrame(data)
            # Load into Pandas DataFrame
            excel_buffer = BytesIO()

            # Use ExcelWriter and specify a sheet name
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                # Ensure at least one visible sheet is written
                if not df.empty:
                    df.to_excel(writer, index=False, sheet_name='Data')
                else:
                    # Create an empty sheet with headers only
                    pd.DataFrame(columns=["name", "price"]).to_excel(writer, index=False, sheet_name='Data')

            # Seek to the beginning of the BytesIO buffer
            excel_buffer.seek(0)

            # Create the HTTP response
            response = HttpResponse(
                excel_buffer.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; filename=StockVScanningDiffExcessData.xlsx'

            return response



    return render(request,'DBS&S.html')

def short(request):
#     location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c')
#     qs = StockData.objects.values(
#         'EANCODE', 'BARCODE', 'ITEMNAME', 'SIZE', 'BRAND','SECTION', 'MRP'
#     ).annotate(
#         stock_sum=Sum('CLOSINGSTOCK', output_field=IntegerField()),   # force numeric
#         home_loctionrecords=Subquery(location_count, output_field=IntegerField())
#     )
#  # RESULT1
#     result1 = qs.annotate(
#         home_stockdata=Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
#         home_loctionrecords=Coalesce(F('home_loctionrecords'), Value(0), output_field=IntegerField()),
#         difference=ExpressionWrapper(
#             F('home_loctionrecords') - Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
#             output_field=IntegerField()  # enforce integer output
#         )
#     ).filter(difference__lt=0)  # 👈 correct way

    # stockDataRec = StockData.objects.all().values()
    return render(request, "shortFile.html")

def excess(request):
    # location_count = loctionRecords.objects.filter( add_item_list=OuterRef('EANCODE') ).values('add_item_list').annotate( c=Count('id') ).values('c')
    # qs = StockData.objects.values(
    #     'EANCODE', 'BARCODE', 'ITEMNAME', 'SIZE', 'BRAND','SECTION', 'MRP'
    # ).annotate(
    #     stock_sum=Sum('CLOSINGSTOCK', output_field=IntegerField()),   # force numeric
    #     home_loctionrecords=Subquery(location_count, output_field=IntegerField())
    # )
    # result2 = qs.annotate(
    # home_stockdata=Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
    # home_loctionrecords=Coalesce(F('home_loctionrecords'), Value(0), output_field=IntegerField()),
    # difference=ExpressionWrapper(
    #     F('home_loctionrecords') - Coalesce(F('stock_sum'), Value(0), output_field=IntegerField()),
    #     output_field=IntegerField()  # enforce integer output
    # )
    # ).filter(difference__gt=0)  # 👈 correct way
    # res = StockData.objects.values('BARCODE','ITEMNAME','SIZE','SECTION','MRP')
    # df = pd.DataFrame(list(res))
    # print(df)
    result = masterFile.objects.all()

    return render(request, "excess.html",{"result":result,})
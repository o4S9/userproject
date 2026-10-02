from django.db import models

# Create your models here.

class YourModel(models.Model):
    location  = models.CharField(max_length=100)
    addl      = models.CharField(max_length=100)
    itemcode  = models.CharField(max_length=100)
    itemname  = models.CharField(max_length=100)
    size      = models.CharField(max_length=50)
    qty       = models.IntegerField()

class Scannerinput(models.Model):
    addl = models.CharField(max_length=100)


class Barcode(models.Model):
    code = models.CharField(max_length=100)
    scanned_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.code

class teacher(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class dataEntry(models.Model):
    my_date = models.DateField()  # Stores only the date
    my_text = models.CharField(max_length=200)


class location(models.Model):
    my_date = models.DateField(auto_now_add=True)  # Stores only the date
    loc_vise = models.CharField(max_length=200)
    def __str__(self):
        return self.loc_vise
    
class scanningFile(models.Model):
    file = models.FileField(upload_to="scanningFile")

class loctionRecords(models.Model):
    my_date = models.DateField(auto_now_add=True)  # Stores only the date
    loc_rec = models.CharField(max_length=200, default="Not Assigned", null=True, blank=True)
    add_item_list = models.CharField(max_length=200, default="0", null=True, blank=True)

class ExcessRecordScanning(models.Model):
    my_date = models.DateField(auto_now_add=True)  # Stores only the date
    loc_rec = models.CharField(max_length=200, default="Not Assigned", null=True, blank=True)
    add_item_list = models.CharField(max_length=200, default="Not Soire", null=True, blank=True)

class ExcessScanning(models.Model):
    my_date = models.DateField(auto_now_add=True)  # Stores only the date
    loc_rec = models.CharField(max_length=200, default="Not Assigned", null=True, blank=True)
    add_item_list = models.CharField(max_length=200, default="Not Soire", null=True, blank=True)


class File(models.Model):
    file = models.FileField(upload_to="files")

class masterFile(models.Model):
    file = models.FileField(upload_to="masterfiles")

class MasterData(models.Model):
    my_date     = models.DateField(auto_now_add=True) 
    ADDL        = models.CharField(max_length=100)
    ITEMCODE	= models.CharField(max_length=100)
    ITEMNAME	= models.CharField(max_length=100)
    SIZE	    = models.CharField(max_length=100)
    MRP	        = models.CharField(max_length=100)
    BRANDNAME   = models.CharField(max_length=100)
    SECTION     = models.CharField(max_length=100)
    BASICRATE   = models.CharField(max_length=100)
    SEASON      = models.CharField(max_length=100)
    COLOURS     = models.CharField(max_length=100)

class stockFile(models.Model):
    file = models.FileField(upload_to="stockfile")

class MasterData(models.Model):
    my_date     = models.DateField(auto_now_add=True) 
    ADDL        = models.CharField(max_length=100)
    ITEMCODE	= models.CharField(max_length=100)
    ITEMNAME	= models.CharField(max_length=100)
    SIZE	    = models.CharField(max_length=100)
    MRP	        = models.CharField(max_length=100)
    BRANDNAME   = models.CharField(max_length=100)
    SECTION     = models.CharField(max_length=100)
    BASICRATE   = models.CharField(max_length=100)
    SEASON      = models.CharField(max_length=100)
    COLOURS     = models.CharField(max_length=100)

class StockData(models.Model):
    my_date         = models.DateField(auto_now_add=True) 
    BRANCHCODE	    =models.CharField(max_length=200)
    BRANCHNAME	    =models.CharField(max_length=200) 
    COMPANY	        =models.CharField(max_length=200)
    ARTICLENO	    =models.CharField(max_length=200)
    ITEMNAME	    =models.CharField(max_length=200)
    COLOURS	        =models.CharField(max_length=200)
    BARCODE	        =models.CharField(max_length=200)
    EANCODE	        =models.CharField(max_length=200)
    SIZE	        =models.CharField(max_length=200)
    SECTION	        =models.CharField(max_length=200)
    BRAND           =models.CharField(max_length=200)
    SEASON          =models.CharField(max_length=200)
    ITEM_DESC       =models.CharField(max_length=200)
    GROUP5_GRP1	    =models.CharField(max_length=200)
    GENDER	        =models.CharField(max_length=200)
    GST	            =models.CharField(max_length=200)
    CLOSINGSTOCK    =models.CharField(max_length=200)	
    COST	        =models.CharField(max_length=200)
    MRP	            =models.CharField(max_length=200)
    CLOSINGVALUECOST=models.CharField(max_length=200)
    CLOSINGVALUEMRP =models.CharField(max_length=200)
    GODOWNNAME	    =models.CharField(max_length=200)
    ITEMNAME_SHADESHORTNAME_PACKGROUPNAME =models.CharField(max_length=200)


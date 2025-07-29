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

class loctionRecords(models.Model):
    my_date = models.DateField(auto_now_add=True)  # Stores only the date
    loc_rec = models.CharField(max_length=200, default="Not Assigned", null=True, blank=True)
    add_item_list = models.CharField(max_length=200, default="Not Soire", null=True, blank=True)


# class AddData(models.Model):
#     location  = models.CharField(max_length=100)
#     addl      = models.CharField(max_length=100)
#     itemcode  = models.CharField(max_length=100)
#     itemname  = models.CharField(max_length=100)
#     size      = models.CharField(max_length=50)
#     qty       = models.IntegerField()


class File(models.Model):
    file = models.FileField(upload_to="files")

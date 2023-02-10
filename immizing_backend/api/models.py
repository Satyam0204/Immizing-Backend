from django.db import models

# Create your models here.

class Address(models.Model):
    Street=models.TextField(max_length=500)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=6)

class ForeignNationalInfo(models.Model):
    FirstName=models.CharField(max_length=500)
    MiddleName=models.CharField(max_length=500,blank=True)
    LastName=models.CharField(max_length=500)
    Date_of_Birth=models.DateField()
    Email=models.EmailField()
    Phone=models.CharField(max_length=10)
    SSN=models.CharField(max_length=500)
    presentAddress=models.ForeignKey(Address,on_delete=models.CASCADE,null=True,related_name='presentAddress')
    previousAddresses=models.ManyToManyField(Address,blank=True,related_name='previousAddress')
    mailingAddress=models.ForeignKey(Address,on_delete=models.CASCADE,null=True,blank=True,related_name='mailingAddress')
    copyprevtopresentAddr=models.BooleanField(default=0)
    
    def prevToCurrAddr(self):
        if(self.copyprevtopresentAddr):
            self.previousAddresses.add(self.presentAddress)

    def __str__(self):
        return self.FirstName+" "+self.LastName

    
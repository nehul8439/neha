from django.db import models

# Create your models here.
class User(models.Model):
	username=models.CharField(max_length=20)
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=20)
    
	
	class Meta:
		db_table='User'

# Create your models here.


class User(models.Model):
    gender_choice = (
        ('M', 'male'),
        ('F', 'female'),
        ('o', 'other'),
    )
    yourname=models.CharField(max_length=50)
    adhar=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)
    mobile=models.CharField(max_length=11)
    address=models.TextField()
    city=models.CharField(max_length=50)
    dob=models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=50,
                              choices=gender_choice,
                              null=True)

    def __str__(self):
        return self.yourname


class Fulldesign(models.Model):
    gender_choice = (
        ('M', 'male'),
        ('F', 'female'),
        ('o', 'other'),
    )
    name=models.CharField(max_length=50)
    adhar=models.CharField(max_length=20)
    work=models.CharField(max_length=50)
    mail=models.EmailField()
    contact=models.CharField(max_length=11)
    address=models.TextField()
    city=models.CharField(max_length=50)
    age=models.CharField(max_length=2)
    pic=models.ImageField(upload_to='picture',null=True,blank=True)
    gender=models.CharField(max_length=50,
                             choices=gender_choice,
                             null=True)

    def __str__(self):
        return self.name
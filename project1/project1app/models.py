from django.db import models

# Create your models here.
class Client(models.Model):
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=256)
    phone=models.IntegerField()

    def __str__(self):
        return self.email

class Owner(models.Model):
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    hotelname=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.hotelname

class Restaurant(models.Model):
    hotelname=models.ForeignKey('Owner',on_delete=models.CASCADE)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=250)
    phone=models.IntegerField()
    about=models.CharField(max_length=800)
    logo=models.ImageField(max_length=255,upload_to='project1app/media')
    image=models.ImageField(max_length=255,upload_to='project1app/media')
    numberSeats=models.IntegerField()

class Review(models.Model):
    hotelname=models.ForeignKey('Owner',on_delete=models.CASCADE)
    email=models.EmailField(max_length=250)
    food=models.CharField(max_length=1)
    ambience=models.CharField(max_length=1)
    hospitality=models.CharField(max_length=1)
    rating=models.CharField(max_length=1)
    review=models.CharField(max_length=250)

class Reservation(models.Model):
    hotelname=models.ForeignKey('Owner',on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    phone=models.IntegerField()
    numberPeople=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    message=models.CharField(max_length=250)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    Email= models.EmailField()
    message=models.CharField(max_length=250)

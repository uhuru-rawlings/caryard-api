from django.db import models

# Create your models here.

class Registration(models.Model):
    useremail = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return self.useremail

class Lastlogin(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    last_login = models.DateTimeField()

    class Meta:
        db_table='Lastlogin'

    def __str__(self):
        return self.user.username

class Profiles(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    contact = models.CharField(max_length=13)
    date_added = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Profiles'

    def __str__(self):
        return self.contact
class Companies(models.Model):
    companyname = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Companies'

    def __str__(self):
        return self.companyname

class CarModels(models.Model):
    modelname = models.CharField(max_length=100)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CarModels'

    def __str__(self):
        return self.modelname

class Cars(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    carmodel = models.CharField(max_length=100)
    years_of_service = models.IntegerField()
    Fuelconsumption = models.CharField(max_length=300)
    description = models.TextField(max_length=6000)

    class Meta:
        db_table = 'Cars'

    def __str__(self):
        return self.carmodel
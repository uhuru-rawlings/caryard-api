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
    user = models.ForeignKey(Registration, CASCADE=models.CASCADE)
    last_login = models.DateTimeField()
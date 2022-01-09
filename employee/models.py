from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=200)
    ename = models.CharField(max_length=200)
    eemail = models.CharField(max_length=200)
    econtact = models.CharField(max_length=200)

    class Meta:
        db_table = "employees"


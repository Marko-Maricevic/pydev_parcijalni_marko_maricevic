from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=150)
    vat_id = models.CharField(max_length=20)
    street = models.CharField(max_length=155)
    city  = models.CharField(max_length=150)
    country = models.CharField(max_length=150)


    name = models.CharField(max_length=150,
                             null=False,
                             blank=False)
    vat_id = models.TextField(max_length=20,
                              null=False,
                                blank=False)
    street = models.CharField(max_length=150,
                              null=True,
                              blank=True)

    city = models.CharField(max_length=150,
                              null=True,
                              blank=True,)
    country = models.CharField(max_length=150,
                              null=True,
                              blank=True,)
    
    def __str__(self):
        return self.name
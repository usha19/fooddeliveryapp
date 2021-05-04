from django.db import models
import os
# Create your models here.
class Food(models.Model):
    #book name
    name=models.CharField(max_length=100)
    #author name
    price=models.FloatField()
    #book description
    description=models.TextField()
    #storing book image
    picture=models.ImageField()
    #to store the bookprice
    
    
    #to display object in string format
    def __str__(self):
        return self.name

class Customer(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	email=models.EmailField()
	phone=models.IntegerField() 
	ordered_product=models.FileField()

	class Meta:
		db_table='Customer'

	def __str__(self):

		return self.name
	def get_absolute_image(self):
		return os.path.join('/media',self.ordered_product.name)

	'''def get_absolute_image(self):

    	return os.path.join('/media',self.profile_picture.name)'''

    

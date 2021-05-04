from django import forms
#importing book attribute to add them to form
from food.models import Food
from food.models import Customer

class FoodForm(forms.ModelForm):
    
    class Meta:
        
        model=Food
        fields='__all__'

'''
BookForm class is the form class which represents the ModelForm.
It has Meta class , we define which model to be used to make form.

The fields denote the actual form fields where we want input from user.
'''        
class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=[
			'name',
			'address',
			'email',
			'phone',
			'ordered_product',
		]

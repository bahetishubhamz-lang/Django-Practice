from django import forms
from .models import Student_Data

class StudentForm(forms.ModelForm):
   class Meta:
         model=Student_Data
         fields=['name','email','age']  
    
    
   def clean_age(self):
    age=self.cleaned_data.get('age')
    if age < 18:
      raise forms.ValidationError("age is less than 18") 
    return age
from django.forms import ModelForm, widgets
from .models import *

class StudentForm(ModelForm):
    
    class Meta:
        model = Student
        fields = "__all__"
        # widgets = {
        #     'name': widgets.TextInput(attrs={'class':'form-control'}),
        #     'roll': widgets.NumberInput(attrs={'class':'form-control'})
        # }
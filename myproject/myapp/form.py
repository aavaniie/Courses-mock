from django  import forms
from .models import *

class Courseform(forms.ModelForm):
    class Meta:
        model = Course
        # fields = "__all__"
        fields = ["name","tutor"]
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if " " in name:
            raise forms.ValidationError("Enter a valid Name")
        return name
    


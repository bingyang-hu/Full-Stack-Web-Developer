from django import forms
from AppTwo.models import User


# connect form to the model
class NewUserForm(forms.ModelForm):
    class Meta():
        model=User   # Form will be linked to User model
        fields='__all__'

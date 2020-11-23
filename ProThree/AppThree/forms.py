from django import forms
from django.core import validators




# def check_for_z(value):
#     if value[0].lower !='z':
#         raise forms.ValidationError("Need to start with Z!")

class FormName(forms.Form):

    name = forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    verify_email=forms.EmailField(label='Enter your email again')
    # botcatcher=forms.CharField(required=False,      # this field will only be visible backend.
    #                             widget=forms.HiddenInput, #Not visible to user but only backend.
    #                             validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self): # clean is a key word. clean_fieldthatyouwillcheck!
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.VlidationError("GOTCHA BOT!")
    #     return botcatcher

    def clean(self):  # clean for the entire form

        all_clean_data = super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email !=  vmail:
            raise forms.ValidationError("MKAE SURE EMAILS MATCH!")
# What is a bot?

# Bot will not look at the weboage but the HTML directly so the botcatcher
# will fill out the botcatcher filed automatically while the human won't because
# this field is hidden inside the webpage.

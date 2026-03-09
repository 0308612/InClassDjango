from django import forms

class checkForm(forms.Form):
    isVET = forms.CheckboxInput()

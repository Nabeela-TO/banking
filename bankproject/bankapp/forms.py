
from django import forms
from .models import  Registration


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        templates = 'newpage.html'
















# class Material(forms.Form):
#     class Meta:
#         model = Material
#         fields = ['debit_card', 'credit_card', 'cheque_book']
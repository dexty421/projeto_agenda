from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from . import models


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(
        attrs={
            'accept':'image/*'
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','phone','email','description','category','picture',
            )
        widgets = {
            'first_name':forms.TextInput(
                attrs={
                    'class':'classe a classe b',
                    'placeholder': 'Primeiro nome'
                }
            )
            ,
            'last_name': forms.TextInput(
                attrs={
                    'placeholder':'Segundo nome'
                }
            ),
            'phone':forms.TextInput(
                attrs={
                    'placeholder': 'Telefone'
                }
            )

        }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError('os nomes estão iguais', code= 'invalid')

            self.add_error('last_name',msg)
            self.add_error('first_name', msg)
            
        
        # self.add_error(
        #     'first_name',ValidationError(
        #         'Mensagem de erro', 
        #         code = 'invalid'
        #     )
        # )
        return super().clean()
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
             'first_name',ValidationError(
                'veio do add_error', 
                 code = 'invalid'
                )
            )
        return first_name
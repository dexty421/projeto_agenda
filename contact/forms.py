#importação para formulario
from django import forms
from django.core.exceptions import ValidationError
#importações para usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
import re


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

class RegisterForm(UserCreationForm):
        first_name = forms.CharField(min_length= 3 ,
                                      required=True ,
                                    )
                                #required = obrigatorio esse campo   
        email = forms.EmailField(required=True, max_length=150)
        
        class Meta:
             model = User
             fields = (
                  'first_name',
                  'last_name',
                  'email',
                  'username',
                  'password1',
                  'password2',
             )

        def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')
            #saber se o primeiro nome contem numeros entre ele
            if isinstance(first_name,str):
                 if re.search(r'\d', first_name):
                    self.add_error(
                      'first_name',
                      ValidationError(
                           f"O nome {first_name} contem numeros",
                           code='invalid'
                        )
                    )
            return first_name

        def clean_email(self):
            email = self.cleaned_data.get('email') 


            #logica para saber se o email já foi cadastrado no banco de dados
            if User.objects.filter(email = email).exists():
                 self.add_error(
                    #o campo email, poderia ser outro campo
                      'email',
                      #Levantar erro de validação no campo
                      ValidationError(
                           "Email já cadastrado",
                           code='invalid'
                           )
                 )
            return email    
from django.db import models
#Importando para conseguir pegar a data e hora exata
from django.utils import timezone

from django.contrib.auth.models import User 
# Create your models here.



class Category(models.Model):
    #class Meta é para mudar o nome do model no admin do django
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)  
    def __str__(self) -> str:
        return f'{self.name} '
    

    #$$ O ID DOS CONTATOS SERÃO CRIADAS AUTOMATICAMENTE NO DJANGO $#
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
                                            #para poder criar sem passar esse valor
                                            #coloca o blank = True
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField( max_length=254,blank=True)
                                    #timezone.now pega os dados de data exatos
                                    # de quando foi registrado   
    created_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
                                    #upload_to ,estou indicando pra que pasta
                                    #essa imagem vai, que esta no settings MEDIA
    picture = models.ImageField(blank=True , upload_to='pictures/%Y/%m')
                                        # set_null = contatos que tem uma categoria
                                        # e apagar esse categoria, no campo ficara null
    category = models.ForeignKey(Category, 
                                 on_delete=models.SET_NULL
                                 ,blank=True
                                 ,null=True
                                 )
    
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null = True)

    #aqui altera como eu visualizo os dados no servidor admin do django
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

 
    
 
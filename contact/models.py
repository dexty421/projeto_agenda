from django.db import models
#Importando para conseguir pegar a data e hora exata
from django.utils import timezone
# Create your models here.
             #$$ O ID VAI SER CRIADO AUTOMATICAMENTE NO DJANGO $#
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

    #aqui altera como eu visualizo os dados no servidor admin do django
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
 
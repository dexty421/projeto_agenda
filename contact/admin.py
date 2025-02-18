from django.contrib import admin
from contact.models import Category, Contact
# Register your models here.
#configurando o model criado no models.py aqui
# colocando o mesmo nome da classe, só que com Admin ex:ContactAdmin,ClienteAdmin
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     #como aparece no banco de dados admin la
    list_display = 'id','first_name','last_name','phone','category', 'show',
     # tem a função de retornar em ordem, pelos parametros que vc colocou
                                # se vc colocar um - dentro do nome da string
                                # ele vai ordenar por ordem descrescente 
                                # ex: '-id' ou '-last_name'
    ordering = 'last_name',
        # list_filter filtra por data no admin django
    # list_filter = 'created_date',
        #search_fields filtra pelos campos colocados nessa tupla abaixo
    search_fields = 'id','last_name','first_name',
    list_per_page = 10
    list_max_show_all = 200
    # consegue editar dados mais facilmente com essa opção
    list_editable = 'last_name','phone','show',
    #deixar linkavel
    list_display_links = 'first_name', 
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
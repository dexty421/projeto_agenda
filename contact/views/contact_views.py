from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
# Create your views here.

def index(request):
                              #filtra os contatos que estão com show = True
                              #esse show está em models.py
    contacts = Contact.objects.filter(show = True).order_by('-id')[10:20]
                                                    #ordena pelo primeiro nome       
    context = {
        'contacts' : contacts,
        'site_title':'Contatos Agenda'
        }

    return render(
        request,
     'contact/index.html',
     context
     )
        #recebe o id do contato, para ir para pagina de contato
def contact(request,contact_id):
                                    #get filtra pelo id especifico
    # single_contact = Contact.objects.filter(id=contact_id).first() ||  
    single_contact = get_object_or_404(Contact,id=contact_id, show = True)
    #if para caso não encontre o contato, ele retorna um erro 404
    
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'
                                                        
    context = {
        'contact' : single_contact,
        'site_title': contact_name,

        }

    return render(
        request,
     'contact/contact.html',
     context
     )
def search(request):
    #pesquisando contatos             #.strip() apaga espaços do começo e fim
    search_value = request.GET.get('q','').strip()
    # se não digitar nada volta para o index
    if search_value == '':
        return redirect('contact:index')
    #Logica da filtragem aqui                          
    contacts = Contact.objects\
        .filter(show = True)\
        .filter(
        Q(first_name__icontains = search_value) |    
        Q(last_name__icontains = search_value)|
        Q(email__icontains = search_value)|
        Q(phone__icontains = search_value)
        )\
        .order_by('-id')                    #A função Q no django permite usar
                                            # para buscar em 4 campos ao mesmo tempo
                                            # como se fosse um 'OR' mas ainda precisa do | 
                                            # Para usar como se fosse and retire o Q, os parentes
                                            # e coloque a virgula    
    #  print(contacts.query)                                                                                      
    context = {
        'contacts' : contacts,
        'site_title':'Search'
        }

    return render(
        request,
     'contact/index.html',
     context
     )

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from contact.models import Contact
# Create your views here.

def index(request):
                              #filtra os contatos que estão com show = True
                              #esse show está em models.py
    contacts = Contact.objects.filter(show = True).order_by('-id')[10:20]
                                                    #ordena pelo primeiro nome       
    context = {
        'contacts' : contacts,
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
    
    
                                                        
    context = {
        'contact' : single_contact,
        }

    return render(
        request,
     'contact/contact.html',
     context
     )
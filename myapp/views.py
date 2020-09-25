from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponseRedirect


# Create your views here.

def acceuil(request):
    return render(request, 'html/acceuil.html')


def activite(request):
    return render(request, 'html/activite.html')


def electricite(request):
    return render(request, 'html/electricite.html')


def batiment(request):
    return render(request, 'html/batiment.html')


def plombier(request):
    return render(request, 'html/plombier.html')


def maintenance(request):
    return render(request, 'html/maintenance.html')


def vente(request):
    return render(request, 'html/vente.html')


def contact(request):
    context = {}

    if request.method == 'POST':
        form: MessageForm = MessageForm(request.POST)
        
        if form.is_valid():
            form.save(),
            return render(request, 'html/merci.html', context)
            #return HttpResponseRedirect('/thanks/',context)

        else:
            context['errors'] = form.errors.items()

    else:
        form = MessageForm()
        context['form']= form

    return render(request, 'html/contact.html', context)

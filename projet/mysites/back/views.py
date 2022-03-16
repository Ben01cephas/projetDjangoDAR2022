import os
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail

from .models import *
from .forms import *

# Create your views here.
class LoginView(TemplateView):

  template_name = 'index.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)
  
def create_user(request,*args,**kwargs):
    template_name= 'inscription.html'
    if request.method == 'GET':
        form = CustomUserCreationForm(
            initial={
                
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =CustomUserCreationForm(
           request.POST,
           request.FILES,
           initial={
              
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
          print(form.cleaned_data)
          form.save()
          return redirect('/')
        return render(request=request,template_name=template_name,context=context,)
      
def update_user(request,*args,**kwargs):
    template_name= 'users/update_user.html'
    current_user = request.user
    
    
    obj = get_object_or_404(
        User,pk=current_user.id,
        # pk=kwargs.get('pk'),
    )
    if request.method == 'GET':
        form = CustomUserChangeForm(
            initial={
                'last_name':obj.last_name,
                'first_name':obj.first_name,
                'telephone':obj.telephone,
                'adresse':obj.adresse,
                'is_active': obj.is_active,
                'is_fromEsmt': obj.is_fromEsmt,
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =CustomUserChangeForm(
           request.POST,
           request.FILES,
           initial={
                'last_name':obj.last_name,
                'first_name':obj.first_name,
                'telephone':obj.telephone,
                'adresse':obj.adresse,
                'is_fromEsmt': obj.is_fromEsmt,
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
          print(form.cleaned_data)
          obj.last_name = form.cleaned_data['last_name']
          obj.first_name = form.cleaned_data['first_name']
          obj.telephone = form.cleaned_data['telephone']
          obj.adresse = form.cleaned_data['adresse']
          obj.is_fromEsmt = form.cleaned_data['is_fromEsmt']
          obj.save()
          return redirect('/')
        return render(request=request,template_name=template_name,context=context,)
      
def changePassword_user(request,*args,**kwargs):
    template_name= 'users/update_password.html'
    current_user = request.user
    
    
    obj = get_object_or_404(
        User,pk=current_user.id,
    )
    if request.method == 'GET':
        form = passwordChangeForm(obj)
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =passwordChangeForm(obj,
           request.POST,
           request.FILES,
             initial={
            
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
          print(form.cleaned_data)
          user = form.save()
          update_session_auth_hash(request, user)  # Important!
          return redirect('/')
        return render(request=request,template_name=template_name,context=context,)

def index(request, *args, **kwargs):

    template_name = 'index.html'
    test = ''
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/profile')

    context = {
        'test':test
    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def aPropos(request, *args, **kwargs):

    template_name = 'apropos.html'

    context = {

    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def contacts(request, *args, **kwargs):

    template_name = 'contacts.html'

    form = contactForm()
         
    if request.method == 'POST':

        form = contactForm(request.POST)

        if form.is_valid():
            msg_title = 'Abonnement au newlestter'
            msg_content = str(form.cleaned_data.get('email'))
            target_mail = str(form.cleaned_data.get('message'))

            send_mail(
                msg_title,
                target_mail,
                'contact@mydomain.com',
                [msg_content],
                fail_silently=False
            ) 
     

    context = {
        'form':form
    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def homeUser(request, *args, **kwargs):

    template_name = 'users/home.html'

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')

    mesepreuves = Epreuve.objects.all().filter(username=request.user.email)
    epreuves = Epreuve.objects.all()

    obj = Epreuve()
    form = EpreuveForm()

    form = EpreuveForm(request.POST, request.FILES)

    if request.method == 'POST':
        
        if form.is_valid():
            obj.nom_fichier_epreuve = form.cleaned_data.get('fichier_epreuve')
            obj.nom_fichier_correction = form.cleaned_data.get('fichier_correction')
            obj.nom_epreuve = form.cleaned_data.get('nom_epreuve')
            obj.niveau_epreuve = form.cleaned_data.get('niveau_epreuve')
            obj.annee_epreuve = form.cleaned_data.get('annee')
            obj.matiere_epreuve = form.cleaned_data.get('matiere')
            obj.nom_filliere = form.cleaned_data.get('filliere')
            obj.nom_prof = form.cleaned_data.get('nom_du_professeur')
            obj.username = request.user.email
            obj.save()

            return HttpResponseRedirect('/accounts/profile')

    context = {
        'test': 'leTest',
        'mesepreuves':mesepreuves,
        'epreuves':epreuves,
        'form':form
    }
    
    return render(
        request=request,
        template_name=template_name,
        context=context
    )

def epreuve_view(request, *args, **kwargs):
    obj = get_object_or_404(
        Epreuve,
        pk=kwargs.get('pk')
    )

    epreuve = Epreuve.objects.get(id_epreuve=obj.id_epreuve)
    pepreuve = str(epreuve.nom_fichier_epreuve)

    try:
        filepath = os.path.join('', pepreuve)
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    except:
        return HttpResponseNotFound("Fichier non trouvé")

    

def correction_view(request, *args, **kwargs):
    obj = get_object_or_404(
        Epreuve,
        pk=kwargs.get('pk')
    )

    epreuve = Epreuve.objects.get(id_epreuve=obj.id_epreuve)
    pepreuve = str(epreuve.nom_fichier_correction)

    try:
        filepath = os.path.join('', pepreuve)
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    except:
        return HttpResponseNotFound("Fichier non trouvé")

def delete_epreuve(request, *args, **kwargs):
    obj = get_object_or_404(
        Epreuve,
        pk=kwargs.get('pk')
    )
    
    epreuve = Epreuve.objects.get(id_epreuve=obj.id_epreuve)
    epreuve.delete()
    epreuve.nom_fichier_epreuve.delete(save=False)
    epreuve.nom_fichier_correction.delete(save=False)   

    return HttpResponseRedirect('/accounts/profile')
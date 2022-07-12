from urllib import response
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.shortcuts import redirect, render

#Clases para el login
from django.contrib.auth.views import LoginView, LogoutView
from .form import * #Asi importamos todos los formularios 


#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView




class Login(LoginView):

    template_name = "src/login.html"
    #template_name = "plantillas_viejas/login copy.html"
    form_class = loginForm

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            print("Estas autenticado y vas al INDEX.HTML")
            

        else:
            print(request.user)
            print("No estas autenticado, eres un usuario anonimo")
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print("Metodo:",self.request.method)
        #print(self.form_class())
        #context['titulo'] = "Vouchly"
        context['formRegistro'] = UsuariosForm(self.request.POST or None)
        return context





class Logout(LogoutView):

    template_name = "src/login.html"
    next_page = "src:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        return context
    



class Index(TemplateView):

    template_name = "src/index.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("src:login")

        else:

            print("Estas autenticado GENIAL")
            
            form = LibrosForm()
            if request.method == "POST":
                print("Probando esta vaina> ",request.POST['autor'])
                form = LibrosForm(request.POST)
                if form.is_valid():
                    print("Valido")
                    #form.save()
                    #product = Product()
                    #product.title = form.cleaned_data['title']
                    #product.price = form.cleaned_data['price']
                    #product.description = form.cleaned_data['description']
                    #product.category = form.cleaned_data['category']
                    form.save()
                    return render(request, 'src/index.html', {'form':LibrosForm(),'Libros':Libros.objects.all()})
                else:
                    print("Invalido")
            #print("usuario: ",request.user)
            #print("usuario permisos: ",request.user.get_all_permissions())
            #print(request.user.has_perm('src.ver_zulia'))
            
            
            
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        if self.request.method == "GET":
            context["form"] =LibrosForm()
            context["Libros"] =Libros.objects.all()
            



################ AQUI VA LA LOGICA DE LOS PERMISOS##############
        print("Usuario get: ",self.request.user)
        
        context['usuario'] = self.request.user
        return context



def pruebas(request):


    return render(request, 'pruebas.html', {})




###### APIS ##########




def api_login(request):


    if request.method == 'GET':


        datos={'saludo':'prueba','despedida':'Adios'}
        return JsonResponse(datos)


def PasarDatos(request):

    return response("datos")


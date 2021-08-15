from django.shortcuts import render

# Importamos vistas genericas:
from django.views.generic import TemplateView

# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from e_commerce.models import *

class PruebaView(TemplateView):
    template_name = 'e-commerce/base.html'
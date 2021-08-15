from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *


urlpatterns = [
    # NOTE: e_commerce base:
    path('base', PruebaView.as_view()),
    
    #TODO: Tarea! 
    ]
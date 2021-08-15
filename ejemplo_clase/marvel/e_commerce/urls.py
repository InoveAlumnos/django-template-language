from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *

urlpatterns = [
    # e-commerce base:
    path('variables', VariablesView.as_view(), name='variables'),
    path('variable-contexto', VariableDeContextoView.as_view(), name='variable-contexto'),
    path('for', ForView.as_view(), name='for'),
    path('if', IfView.as_view(), name='if'),
    path('url-origen', UrlOrigenView.as_view(), name='origen'),
    path('url-destino', UrlDestinoView.as_view(), name='destino'),
    path('csrf-form', CsrfTokenFormView.as_view(), name='formulario'),
    path('base', BaseView.as_view(), name='base'),
    path('extendido', ExtendidoView.as_view(), name='extendido'),

    ]
from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *

urlpatterns = [
    # e-commerce base:
    path('hello', PruebaView.as_view()),
    path('text', TextView.as_view()),
    path('links', LinksView.as_view()),
    path('lists', ListsView.as_view()),
    path('button', ButtonsView.as_view()),
    path('table', TableView.as_view()),
    path('form', FormView.as_view()),
    path('image', ImageView.as_view()),
    path('example', ExampleView.as_view()),
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
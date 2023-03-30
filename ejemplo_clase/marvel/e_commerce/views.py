from django.contrib.auth.models import User
from django.shortcuts import render

# Importamos vistas genericas:
from django.views.generic import TemplateView, CreateView


# NOTE: Generamos las vistas genéricas para probar Django Template:

TEST_DIC = {
    'saludo': 'Hola, mi nombre es: ',
    'user': 'INOVE!! '
}

TEST_LIST = ['Hola, ', 'mi ', 'nombre ', 'es ', 'Inove ']


# NOTE: Generamos las vistas genéricas para probar bloques HTML:
class PruebaView(TemplateView):
    template_name = 'e-commerce/hello.html'


class TextView(TemplateView):
    template_name = 'e-commerce/00-text.html'


class LinksView(TemplateView):
    template_name = 'e-commerce/01-links.html'


class ListsView(TemplateView):
    template_name = 'e-commerce/02-listas.html'


class ButtonsView(TemplateView):
    template_name = 'e-commerce/03-buttons.html'


class TableView(TemplateView):
    template_name = 'e-commerce/04-table.html'


class FormView(TemplateView):
    template_name = 'e-commerce/05-form.html'


class ImageView(TemplateView):
    template_name = 'e-commerce/06-images.html'


class ExampleView(TemplateView):
    template_name = 'e-commerce/example.html'


class VariablesView(TemplateView):
    template_name = 'e-commerce/variables.html'


class VariableDeContextoView(TemplateView):
    template_name = 'e-commerce/variable-contexto.html'

    def get_context_data(self, **kwargs):
        '''
        En esta función vamos a agregar más información a nuestro 
        contexto de ejecución para que pueda ser incluido en nuestros templates!
        La variable `context` es funciona como un diccionario, es por ello que vamos a 
        ir agregandole información para luego ser accedida por su key.
        Aquí también podemos interceptar el objeto "request" 
        con los datos de la petición realizada al sitio.
        '''
        context = super().get_context_data(**kwargs)
        # NOTE: Agregamos una lista a nuestro contexto:
        context['prueba_lista'] = [
            'Hola', 'mi nombre es', self.request.user.username]
        
        # NOTE: Agregamos un diccionario a nuestro contexto:
        context['prueba_diccionario'] = {
            'saludo': 'hola, mi nombre es: ', 'usuario': f'{self.request.user.username}'.upper()}
        return context


class ForView(TemplateView):
    template_name = 'e-commerce/for.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['TEST_DIC']=TEST_DIC
        context['TEST_LIST']=TEST_LIST
        return context

# NOTE: Generamos el template base para extender:
class IfView(TemplateView):
    template_name = 'e-commerce/if.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['TEST_DIC']=TEST_DIC
        context['TEST_LIST']=TEST_LIST
        return context

class UrlOrigenView(TemplateView):
    template_name = 'e-commerce/url-origen.html'


class UrlDestinoView(TemplateView):
    template_name = 'e-commerce/url-destino.html'


class CsrfTokenFormView(CreateView):
    '''
    Importante: Utilizamos un CreateView porque éste admite peticiones POST, 
    necesarias para el envío del formulario en este caso.
    Esta clase requiere un modelo y un campo como mínimo para funcionar.
    '''
    model = User
    fields = ['username']
    template_name = 'e-commerce/csrf-form.html'


class BaseView(TemplateView):
    template_name = 'e-commerce/base.html'


class ExtendidoView(TemplateView):
    template_name = 'e-commerce/extendido.html'
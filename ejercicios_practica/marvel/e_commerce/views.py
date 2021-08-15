from django.shortcuts import render

# Importamos vistas genericas:
from django.views.generic import TemplateView, RedirectView, DetailView
 
# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from e_commerce.models import *

# TEST:
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect



# Probamos la vista generica:
class PruebaView(TemplateView):
    template_name = 'e-commerce/base.html'

# NOTE: Generamos las vistas genéricas para probar bloques HTML:

# NOTE: Ejemplos **********************************************************
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(self.request.user)
        user_obj = User.objects.filter(username=self.request.user).first()
        
        context['wishes']= WishList.objects.filter(user_id=user_obj.id)
        context['lista']=[1,2,3,4]
        print(context.get('wishes'))
        # context['wishes'] = WishList.objects.filter(user_id=self.user)
        return context


# NOTE: Páginas del sitio **********************************************************
class LoginUserView(TemplateView):
    template_name = 'e-commerce/login.html'

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/e-commerce/index')
    else:
        form = UserForm()


    return render(request, 'e-commerce/singup.html', {'form': form})

class CartView(TemplateView):
    template_name = 'e-commerce/cart.html'

class DetailsView(TemplateView):
    template_name = 'e-commerce/detail.html'

class IndexView(TemplateView):
    template_name = 'e-commerce/index.html'

class ThanksView(TemplateView):
    template_name = 'e-commerce/thanks.html'

class UpdateUserView(TemplateView):
    template_name = 'e-commerce/update-user.html'

class UserView(TemplateView):
    template_name = 'e-commerce/user.html'

class WishView(TemplateView):
    template_name = 'e-commerce/wish.html'



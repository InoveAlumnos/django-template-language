from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *


from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    # NOTE: e_commerce base:
    path('base', PruebaView.as_view()),

    # NOTE: Manejo de sesión:
    path('',auth_views.LoginView.as_view(template_name='e-commerce/login.html', redirect_authenticated_user=True, redirect_field_name='index'),
    ),
    path('logout',auth_views.LogoutView.as_view( next_page='/e-commerce/index', redirect_field_name='index'),
    ),
    path('singup', register, name='register'),

    # NOTE: Páginas del sitio:
    path('detail', DetailsView.as_view()),
    path('index', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view()),
    path('index/#', IndexView.as_view()),
    path('thanks', ThanksView.as_view()),
    path('update-user', UpdateUserView.as_view()),
    path('user', login_required(UserView.as_view())),
    path('wish', login_required(WishView.as_view())),
    path('cart', login_required(CartView.as_view())),

    # NOTE: Ejemplos de HTML:
    path('text', TextView.as_view()),
    path('links', LinksView.as_view()),
    path('lists', ListsView.as_view()),
    path('button', ButtonsView.as_view()),
    path('table', TableView.as_view()),
    path('form', FormView.as_view()),
    path('image', ImageView.as_view()),
    path('example', ExampleView.as_view()),
    ]
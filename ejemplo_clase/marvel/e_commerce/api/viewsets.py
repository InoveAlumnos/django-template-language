from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

# Librería para manejar filtrado:
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Para manejar paginado:
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

from e_commerce.models import User
from .serializers import UserSerializer, UpdatePasswordUserSerializer


# Genero una clase para configurar el paginado de la API.
class ShortResultsSetPagination(PageNumberPagination):
    page_size = 3   # Cantidad de resultados por página

    # Me va a permitir configurar la cantidad de resultados a mostrar
    # por página.
    page_size_query_param = 'page_size'
    max_page_size = 10


# NOTE: Vemos que ahora los métodos para cada
# método HTTP, en los viewsets directamente
# se los llaman "acciones". Ejemplo: list, create,
# update, retrieve, destroy, etc.
class CustomUserViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Este método permite administrar los permisos según el tipo de
    # acción que se ejecute.
    def get_permissions(self):
        if self.action != 'list':
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def _get_current_user(self):
        return get_object_or_404(
            User, username=self.request.user.username
        )

    def list(self, request):
        return Response(
            data=self.serializer_class(instance=self.queryset, many=True).data,
            status=status.HTTP_200_OK
        )

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                data=user_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=user_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):
        _current_user =  self._get_current_user()

        # Me devuelve la instancia a partir del queryset, en caso
        # de no existir, retorna un código de estado 404.
        _user = get_object_or_404(self.queryset, pk=pk)

        if _current_user != _user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user_serializer = self.serializer_class(
            instance = _user,
            data=request.data
        )
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                data=user_serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=user_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        _current_user =  self._get_current_user()
        _user = get_object_or_404(self.queryset, pk=pk)

        # if _current_user != _user:
        #     return Response(status=status.HTTP_403_FORBIDDEN)

        return Response(
            data=self.serializer_class(
                instance=_user,
                many=False
            ).data,
            status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        self.queryset.filter(pk=pk).delete()
        return Response(
            data={'message': 'the user was deleted successfully'},
            status=status.HTTP_200_OK
        )

    # Al trabajar con Viewsets podemos definir nuestras propias
    # acciones basándonos en los métodos HTTTP.
    @action(
        detail=True,
        methods=['put'],
        name="change-password",
        url_path='change-password'
    )
    def change_password(self, request, pk=None):
        _current_user =  self._get_current_user()
        _user = get_object_or_404(self.queryset, pk=pk)

        if _current_user != _user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        _user_serializer = UpdatePasswordUserSerializer(
            instance=_user,
            data=request.data,
            partial=True
        )
        # `raise_exception=True` evito de realizar la condición de la línea
        # 48, pero de todas maneras genero una excepción si hay un problema
        # con la validación de los datos.
        _user_serializer.is_valid(raise_exception=True)
        _user_serializer.save()
        return Response(
            data=_user_serializer.data,
            status=status.HTTP_200_OK
        )


# Ahora veamos que sucede si los viewsets los
# heredamos de ModelViewSet.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    # NOTE: Con el siguiente atributo puedo administrar que tipo
    # de métodos permite esta view.
    # http_method_names = ['get', 'post', 'put', 'delete']
    queryset = serializer_class.Meta.model.objects.all()


class FilteringBackendUserViewSet(viewsets.ModelViewSet):
    '''
    Vista de API basada en Clase que permite manejar
    el filtrado, búsqueda, paginado y orden de los resultados del
    listado de la API.
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    # NOTE: Habilito sólo el método 'GET' para esta view.
    http_method_names = ('get',)
    queryset = serializer_class.Meta.model.objects.all()

    # NOTE: Utilizo el tipo de filtro.
    # filter_backends = (DjangoFilterBackend,)
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    # NOTE: Selecciono los campos a filtrar.
    # filterset_fields = ('id', 'username', 'email', 'is_staff')
    filterset_fields = {
        "id": ('gte',),
        "username": ("contains",),
        "first_name": ("contains",),
        "last_name": ("exact",),
        "email": ('exact', 'contains'),
        "is_staff": ('exact',)
    }

    # Genero un Paginado
    pagination_class = LimitOffsetPagination    # ShortResultsSetPagination PageNumberPagination

    # Para buscar el valor en los campos seleccionados.
    # NOTE: se requiere `SearchFilter`.
    search_fields = ('username', 'first_name', 'last_name')

    # Permite ordenar el listado por los campos seleccionados.
    # NOTE: se requiere `OrderingFilter`.
    ordering_fields = ('pk', 'username')
    ordering = ('pk',)  # ('-pk',)


class FilteringUserViewSet(viewsets.GenericViewSet):
    '''
    Vista de API basada en Clase que permite manejar
    el filtrado, búsqueda, y orden de los resultados del
    listado de la API utilizando el ORM de Django.
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = serializer_class.Meta.model.objects.all()

    # NOTE: Habilito sólo el método 'GET' para esta view.
    http_method_names = ('get',)

    def get_queryset(self):
        # Obtengo el queryset llamando al método get_queryset mediante super.
        queryset = super(FilteringUserViewSet, self).get_queryset()

        # Obtengo los parámetros dinámicos que me llegan en la URL
        # cuando el usuario realiza una petición de tipo GET.
        # NOTE: Recordar que otra forma de hacerlo es:
        # _pk: self.request.GET.get('id')
        _pk = self.request.query_params.get('id')
        _username = self.request.query_params.get('username')
        _is_staff = self.request.query_params.get('is_staff', '').capitalize()
        _search = self.request.query_params.get('search', '')
        _ordering = self.request.query_params.get('ordering', 'username')

        queryset = queryset.filter(
            Q(username__icontains=_username) &
            Q(
                Q(username__icontains=_search) |
                Q(first_name__icontains=_search) |
                Q(last_name__icontains=_search)
            )
        ).order_by(_ordering)

        # Realizo el filtrado según los parámetros que me pasen.
        if _pk:
            queryset = queryset.filter(pk=int(_pk))
        if _is_staff:
            queryset = queryset.filter(is_staff=eval(_is_staff))

        return queryset

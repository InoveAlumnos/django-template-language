from django.urls import path, include
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.api.api_views import *

urlpatterns = [
    # User APIs:
    path('user/login/', LoginUserAPIView.as_view()),

    # APIs de Marvel
    path('get-comics/',get_comics),
    path('purchased-item/',purchased_item),
    
    # Comic API View:
    path('comics/get', GetComicAPIView.as_view()),
    path('comics/<int:pk>/get', GetOneComicAPIView.as_view()),
    path(
        'comics/marvel/<int:marvel_id>/get',
        GetOneMarvelComicAPIView.as_view()
    ),
    path('comics/post', PostComicAPIView.as_view()),
    path('comics/get-post', ListCreateComicAPIView.as_view()),
    path('comics/<int:pk>/get-update', RetrieveUpdateComicAPIView.as_view()),
    path('comics/<int:marvel_id>/update', UpdateComicAPIView.as_view()),
    path('comics/<int:pk>/delete', DestroyComicAPIView.as_view()),

    # TODO: Wish-list API View
    path('wish/get', GetWishListAPIView.as_view()),
    path('wish/post', PostWishListAPIView.as_view()),
    path('wish/<int:comic_id>/update', UpdateWishListAPIView.as_view()),
    path('wish/<int:comic_id>/delete', DeleteWishListAPIView.as_view()),
    path('favs/<str:username>/get', GetUserFavsAPIView.as_view()),

    # User API Viewsets:
    path('api/', include('e_commerce.api.routers')),
]
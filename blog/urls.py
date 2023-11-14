from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('formulaire/', views.formulaire, name='formulaire'),
    path('',views.base, name ='base'),
    path('modifier_joueur/<int:numero>/', views.modif_joueur, name='modif_joueur'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
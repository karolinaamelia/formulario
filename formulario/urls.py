from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, formulario_list, formulario_from, formulario_update, formulario_delete


urlpatterns = [
    path('', index, name='index'),
    path('formulario', formulario_from, name='formulario'),
    path('listagem', formulario_list, name='listagem'),
    path('update/<int:id>/', formulario_update, name="formulario_update"),
    path('delete/<int:id>/', formulario_delete, name="formulario_delete")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

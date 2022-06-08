from django.contrib import admin
from .models import FormularioModel


@admin.register(FormularioModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ("imagem_original", "valor", "data", "descricao", "imagem_tratada", "imagem_copilada",)

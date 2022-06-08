from django.db import models


class FormularioModel(models.Model):
    imagem_original = models.FileField("Imagem Original", upload_to="%Y/%m/%d/")
    valor = models.DecimalField("Valor", max_digits=7, decimal_places=2, null=True, blank=True)
    data = models.DateField("Data", auto_now=False, null=True, blank=True)
    descricao = models.CharField("Descrição", max_length=255, null=True, blank=True)
    imagem_tratada = models.FileField("Imagem Tratada", upload_to="%Y/%m/%d/")
    imagem_copilada = models.FileField("Imagem Copilada", upload_to="%Y/%m/%d/")

    def __str__(self):
        return str(self.data)

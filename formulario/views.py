from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import FormularioModelForm
from .models import FormularioModel


def index(request):
    return render(request, 'index.html')


def formulario_from(request):
    form = FormularioModelForm()

    if str(request.method) == 'POST':
        form = FormularioModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enviado com sucesso')
            form = FormularioModelForm()
        else:
            messages.error(request, 'Erro ao enviar')

    context = {
        'form': form
    }
    return render(request, 'formulario/formulario_from.html', context)


def formulario_list(request):

    formulario_objts = FormularioModel.objects.all()

    context = {
        'formulario': formulario_objts
    }

    return render(request, 'formulario/formulario_list.html', context)


def formulario_update(request, id):
    formulario_id = get_object_or_404(FormularioModel, pk=id)
    form = FormularioModelForm(request.POST or None, request.FILES or None, instance=formulario_id)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    return render(request, 'formulario/formulario_update.html', {'form': form})


def formulario_delete(request, id):
    formulario_id = get_object_or_404(FormularioModel, pk=id)
    form = FormularioModelForm(request.POST or None, request.FILES or None, instance=formulario_id)

    if request.method == 'POST':
        form.delete()
        return redirect('listagem')

    return render(request, 'formulario/formulario_delete_confirm.html', {'form': form})




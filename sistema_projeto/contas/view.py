from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def gerenciar_clientes(request):
    if request.method == 'POST':
        if 'cliente_id' in request.POST:
            cliente = get_object_or_404(Cliente, id=request.POST['cliente_id'])
            form = ClienteForm(request.POST, instance=cliente)
        else:
            form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gerenciar_clientes')
    else:
        if 'editar' in request.GET:
            cliente = get_object_or_404(Cliente, id=request.GET['editar'])
            form = ClienteForm(instance=cliente)
        else:
            form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'contas/gerenciar_clientes.html', {'form': form, 'clientes': clientes})

def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('gerenciar_clientes')

from django.shortcuts import render, redirect,get_object_or_404
from .models import OrdemServico
from .forms import OrdemServicoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista_ordens(request):
    ordens = OrdemServico.objects.all()
    return render(request, 'ordensservico.html', {'ordens': ordens})

@login_required
def nova_ordem(request):
    form = OrdemServicoForm(request.POST or None)
    dataProgOrdem = OrdemServico.dataProgramada
    if form.is_valid():
        form.save()
        return redirect('listar')
    else:
        print(form.errors)

    return render(request, 'ordens_form.html', {'form': form})
@login_required
def update_ordem(request, idCriacao):
    ordem = get_object_or_404(OrdemServico, pk=idCriacao)
    form = OrdemServicoForm(request.POST or None,request.FILES or None, instance=ordem)

    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request,'ordens_form.html',{'form':form})
@login_required
def delete_ordem(request, idCriacao):
    ordem = get_object_or_404(OrdemServico, pk=idCriacao)
    form = OrdemServicoForm(request.POST or None, request.FILES or None, instance=ordem)
    if request.method == 'POST':
        ordem.delete()
        return redirect('listar')

    return render(request, 'confirma_delete_ordem.html',{'form':form,'ordem':ordem})
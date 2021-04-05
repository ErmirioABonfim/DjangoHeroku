from django.forms import ModelForm
from .models import OrdemServico


class OrdemServicoForm(ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['id', 'numeroOrdemServico', 'tipoServicos','Turno', 'dataProgramada','dataExecucao','Manutentores', 'tipoManutencao',
                 'status', 'Material','Descricao' ]

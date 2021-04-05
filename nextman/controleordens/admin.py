from django.contrib import admin
from .models import OrdemServico, Manutentor


class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'numeroOrdemServico', 'tipoServicos','Turno','dataCriacao', 'dataProgramada','dataExecucao','Manutentores', 'tipoManutencao',
                 'status','Material', 'imagensAntes', 'imagemDepois','quantidade_material' ]

    list_filter = ['id', 'numeroOrdemServico', 'tipoServicos','Turno','dataCriacao', 'dataProgramada','dataExecucao','Manutentores', 'tipoManutencao',
                 'status', 'Material','quantidade_material']

    search_fields = ['numeroOrdemServico']



class ManutentoresAdmin(admin.ModelAdmin):
    list_display = ['manutentor']

admin.site.register(OrdemServico, OrdemServicoAdmin,)
admin.site.register( Manutentor, ManutentoresAdmin)



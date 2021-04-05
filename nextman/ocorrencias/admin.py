from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ParadaDeMaquina, Funcionario, Maquina
from django.contrib.auth.models import Group
admin.site.site_header= " NextMan | admin "
admin.site.site_title = " NextMan | admin "
admin.site.site_footer = " Soluções em Sistemas"
# Register your models here.



class ParadasDeMaquinaAdmin(admin.ModelAdmin):
    list_display = ['id','tipoServico', 'maquina','tipoManutencao','horaOcorencia','horaReinicio', 'duracao','turno','operador','descricao']
    list_filter =  ['id','tipoServico', 'maquina','tipoManutencao','horaOcorencia','horaReinicio', 'duracao','turno','operador','descricao']
    #list_editable = ['nomeMaquina', 'motivo', 'tipoManutencao', 'dataParada', 'DataReinicio', 'turno','observacoes']
admin.site.register(ParadaDeMaquina,ParadasDeMaquinaAdmin)




class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id','nome', 'funcao']
    list_filter = ['id','nome', 'funcao']

admin.site.register(Funcionario, FuncionarioAdmin)

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ['id','nomeMaquina']
    list_filter = ['id','nomeMaquina']

admin.site.register(Maquina, MaquinaAdmin)
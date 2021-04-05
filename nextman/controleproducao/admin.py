from django.contrib import admin

from .models import ProducaoMaquina
# Register your models here.

class ProducaoMaquinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'Equipamento', 'OrdemProd', 'ProdDia', 'ProdDia', 'ProdDataInicio','ProdDataFim','Operador','Produto']
    list_filter = ['id', 'Equipamento', 'OrdemProd', 'ProdDia', 'ProdDia', 'ProdDataInicio','ProdDataFim','Operador','Produto']
    search_fields = ['Equipamento']



admin.site.register(ProducaoMaquina,ProducaoMaquinaAdmin)
from django.contrib import admin
from .models import Item, Consumo, Compras

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome_item', 'descricao', 'quantidade', 'custo', 'tipoComponente', 'photo' ]
    list_filter = ['nome_item', 'descricao', 'quantidade', 'custo', 'tipoComponente', 'photo' ]
admin.site.register(Item, ItemAdmin)

class ConsumoPecasAdmin(admin.ModelAdmin):
    list_display = ['item','quantidade_consumo','data_consumo', 'requisitante', 'descricao']
admin.site.register(Consumo,ConsumoPecasAdmin)

class CompraPecasAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantidade_compra', 'data_compra', 'descricao']
admin.site.register(Compras,CompraPecasAdmin)
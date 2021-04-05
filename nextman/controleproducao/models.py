from django.db import models
from ocorrencias.models import Maquina,Funcionario
# Create your models here.
class ProducaoMaquina(models.Model):

    Equipamento = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    OrdemProd = models.IntegerField(verbose_name='Ordem De Produção',blank=True, null=True,editable=True)
    ProdDia = models.IntegerField(verbose_name='Produção Do Dia')
    ProdDataInicio = models.DateTimeField(verbose_name='Inicio Produção')
    ProdDataFim = models.DateField(verbose_name='Fim Produção')
    Operador = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    Produto = models.IntegerField(verbose_name='Código Produto')

    class Meta:
        verbose_name = 'Produção de Máquina'
        verbose_name_plural = 'Produção de Máquinas'
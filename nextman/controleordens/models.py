from django.db import models
from ocorrencias.models import Maquina, Funcionario
from  estoquepecas.models import Item

class Manutentor(models.Model):
    manutentor = models.ForeignKey(Funcionario,on_delete=models.CASCADE,verbose_name='Manutentor')
    def __str__(self):
        return str(self.manutentor)

    class Meta:
        verbose_name = 'Manutentor'
        verbose_name_plural = 'Manutentores'

# Create your models here.
class OrdemServico(models.Model):
    TIPO_SERVICOS_CHOICES = (
        ('Preventiva', 'Preventiva'),
        ('Corretiva', 'Corretiva'),
        ('Preditiva', 'Preditiva')
    )
    TIPO_MANUTENCAO_CHOICES = (
        ('ELE', 'ELETRICA'),
        ('MEC', 'MECANICA'),
        ('LUB', 'LUBRIFICACAO'),
        ('CIV', 'CIVIL')
    )
    STATUS_CHOICE = (
        ('Aberta', 'Aberta'),
        ('Fechada', 'Fechada'),
        ('Cancelada', 'Cancelada')
    )

    TURNO_CHOICE = (
        ('A', 'Primeiro'),
        ('B', 'Segundo'),
        ('C', 'Terceiro')
    )

    numeroOrdemServico = models.SmallIntegerField(verbose_name='Numero Ordem Serviço')
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    tipoServicos = models.CharField(max_length=15, blank=True, null=True, choices=TIPO_SERVICOS_CHOICES,verbose_name='Tipo de Manutenção')
    Turno = models.CharField(max_length=30, verbose_name='Turno', choices=TURNO_CHOICE)
    dataCriacao = models.DateField(verbose_name='Criado em', null=True, blank=True, auto_now=True, editable=True)
    dataProgramada = models.DateField(verbose_name='Programado para', null=True, blank=True)
    dataExecucao = models.DateField(verbose_name='Executado em', null=True, blank=True)
    Manutentores = models.ForeignKey(Manutentor, on_delete=models.CASCADE)
    tipoManutencao = models.CharField(max_length=15, verbose_name='Tipo de Manutenção', choices=TIPO_MANUTENCAO_CHOICES,
                                      null=False, blank=False)
    status = models.CharField(max_length=10,verbose_name='Status', choices=STATUS_CHOICE)
    Material = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade_material = models.IntegerField(verbose_name='Quantidade', default=1)
    imagensAntes = models.ImageField(verbose_name='Imagem antes',null=True,blank=True,upload_to="ImagemAntes")
    imagemDepois = models.ImageField(verbose_name='Imagem Depois',null=True, blank=True, upload_to="ImagemDepois")
    Descricao = models.TextField('Descrição Serviço')


    def save(self, *args, **kwargs):
        self.Material.quantidade -= self.quantidade_material
        Item.objects.filter(id=self.Material.id).update(quantidade=self.Material.quantidade)
        super(OrdemServico, self).save(*args, **kwargs)




    def __str__(self):
        # return 'OS: ' + str(self.numeroOrdemServico) + ' - ' + str(self.tipoAtividade) + ' - ' + str(self.tipoManutencao) + ' - ' + str(self.dataProgramacao) + ' - Status: ' + str(self.status)
        return f'OS: {str(self.numeroOrdemServico)} - {str(self.tipoServicos)} - {str(self.tipoManutencao)} - {str(self.dataProgramada)} - Status: {str(self.status)}'

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=30)
    funcao = models.CharField('Função', max_length=30)
    def __str__(self):
        return self.nome

class Maquina(models.Model):
    nomeMaquina = models.CharField('Nome Máquina', max_length=30,unique=True)
    def __str__(self):
        return self.nomeMaquina


class ParadaDeMaquina(models.Model):

    TIPO_MANUTENCAO_CHOICES=(
        ('Corretiva','Corretiva'),
        ('Preventiva','Preventiva'),

    )
    TIPO_SERVICO_CHOICES = (
        ('ELE', 'ELETRICA'),
        ('MEC', 'MECANICA'),
        ('LUB', 'LUBRIFICACAO'),
        ('CIV', 'CIVIL')
    )
    TURNO_CHOICES = (
        ('1°', 'Primeiro'),
        ('2°', 'Segundo'),
        ('3°', 'Terceiro'),
        ('ADM', 'Administrativo')
    )
    # id = models.IntegerField(verbose_name='ID Ocorrência', primary_key=True, null=False, auto_created=True)
    tipoServico = models.CharField(verbose_name='Tipo de Serviço', max_length=30, choices=TIPO_SERVICO_CHOICES, null= True, default='ELETRICA')
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    tipoManutencao = models.CharField(max_length=15,verbose_name='Motivo', choices=TIPO_MANUTENCAO_CHOICES,default='Preventiva',null=True)
    horaOcorencia = models.DateTimeField(verbose_name='Data Ocorencia', auto_now=True, null= True)
    horaReinicio = models.DateTimeField(verbose_name='Data Reinicio',null= True)
    duracao = models.DateTimeField(verbose_name='Duração',null= True)
    turno = models.CharField(verbose_name='Turno', choices=TURNO_CHOICES, max_length=30, null= True)
    operador = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=150, verbose_name='Descrição', null= True)
    def __str__(self):
        return str(self.maquina)






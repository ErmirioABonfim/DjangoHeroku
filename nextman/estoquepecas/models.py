from django.db import models
from ocorrencias.models import Funcionario,ParadaDeMaquina

# Create your models here.
class Item(models.Model):
    TIPO_COMPONENTE = (
        ("Eletrica", "Eletrica"),
        ("Mecanica", "Mecanica"),
        ("Civil", "Civil")
    )
    nome_item = models.CharField(max_length=20, verbose_name='Nome item')
    descricao = models.TextField( verbose_name='Descrição')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    custo = models.DecimalField(verbose_name='Valor',decimal_places=2,max_digits=6)
    tipoComponente = models.CharField(verbose_name='Tipo Componente', max_length=15, choices=TIPO_COMPONENTE, default='Mecanica')
    photo = models.ImageField(verbose_name='foto', upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.nome_item


class Compras(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade_compra = models.IntegerField(verbose_name='Quantidade', default=1)
    data_compra = models.DateField(verbose_name=' Data Da Venda', null=True)
    descricao = models.CharField(verbose_name='Descrição', max_length=100, null=True)



    def save(self, *args, **kwargs):
        self.item.quantidade += self.quantidade_compra
        Item.objects.filter(id=self.item.id).update(quantidade=self.item.quantidade)
        super(Compras, self).save(*args, **kwargs)

    class Meta:
        verbose_name='Compra'
        verbose_name_plural='Compras'

    def __str__(self):
        return str(self.item)

class Consumo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade_consumo = models.IntegerField(verbose_name='Quantidade')
    data_consumo = models.DateTimeField(auto_now_add=True,verbose_name=' Data Do Consumo', null=False)
    requisitante = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)


    def save(self, *args, **kwargs):
        self.item.quantidade -= self.quantidade_consumo
        Item.objects.filter(id=self.item.id).update(quantidade=self.item.quantidade)
        super(Consumo, self).save(*args, **kwargs)




    def __str__(self):
        return str(self.item)


    class Meta:
        verbose_name='Consumo'
        verbose_name_plural='Consumos'
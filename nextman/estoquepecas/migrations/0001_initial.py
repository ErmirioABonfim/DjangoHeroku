# Generated by Django 3.1.7 on 2021-03-31 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ocorrencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_item', models.CharField(max_length=20, verbose_name='Nome item')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('custo', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('tipoComponente', models.CharField(choices=[('Eletrica', 'Eletrica'), ('Mecanica', 'Mecanica'), ('Civil', 'Civil')], default='Mecanica', max_length=15, verbose_name='Tipo Componente')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clients_photos', verbose_name='foto')),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_consumo', models.IntegerField(verbose_name='Quantidade')),
                ('data_consumo', models.DateTimeField(auto_now_add=True, verbose_name=' Data Do Consumo')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoquepecas.item')),
                ('requisitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocorrencias.funcionario')),
            ],
            options={
                'verbose_name': 'Consumo',
                'verbose_name_plural': 'Consumos',
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_compra', models.IntegerField(default=1, verbose_name='Quantidade')),
                ('data_compra', models.DateField(null=True, verbose_name=' Data Da Venda')),
                ('descricao', models.CharField(max_length=100, null=True, verbose_name='Descrição')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoquepecas.item')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
    ]

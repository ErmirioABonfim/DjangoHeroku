# Generated by Django 3.1.7 on 2021-04-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleordens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='numeroOrdemServico',
            field=models.SmallIntegerField(auto_created=True, verbose_name='Numero Ordem Serviço'),
        ),
    ]
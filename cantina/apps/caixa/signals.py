from django.db.models.signals import pre_save, post_save
from django.db.models import F, Sum
from django.dispatch import receiver
from decimal import Decimal

from .models import (
    Lancamento,
    Venda,
    VendaProduto,
)


@receiver(pre_save, sender=VendaProduto)
def update_venda_produtos(sender, instance, **kwargs):
    # preservar valores quando a venda for concluída
    if instance.valor <= 0:
        instance.valor = instance.produto.valor


@receiver(pre_save, sender=Venda)
def update_venda_status(sender, instance, **kwargs):
    instance.pago = instance.total_pago >= instance.total_venda


@receiver(post_save, sender=Lancamento)
@receiver(post_save, sender=VendaProduto)
def update_venda_totais(sender, instance, **kwargs):
    objs = sender.objects.filter(venda=instance.venda)

    if sender is Lancamento:
        instance.venda.total_pago = objs.aggregate(total_pago=Sum("valor"))[
            "total_pago"
        ]
    elif sender is VendaProduto:
        instance.venda.total_venda = objs.annotate(
            valor_total=F("valor") * F("quantidade")
        ).aggregate(total_venda=Sum("valor_total"))["total_venda"]

    instance.venda.save()

from django.db import models
from decimal import Decimal
from cantina.apps.balcao.models import Produto
from cantina.apps.clientes.models import Aluno

from model_utils.models import (
    SoftDeletableModel,
    TimeStampedModel,
)

PAGAMENTO_CHOICES = {
    0: "Dinheiro",
    1: "Débito",
    2: "Crédito",
    3: "Pix",
}


class Venda(SoftDeletableModel, TimeStampedModel):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.DO_NOTHING,
    )

    pago = models.BooleanField(default=False)
    produtos = models.ManyToManyField(Produto, through="VendaProduto")

    total_venda = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal(0),
    )

    total_pago = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal(0),
    )

    def __str__(self) -> str:
        return f"{self.aluno.nome} - R$ {self.total_venda}"


class VendaProduto(SoftDeletableModel, TimeStampedModel):
    venda = models.ForeignKey(
        Venda,
        verbose_name="venda",
        on_delete=models.DO_NOTHING,
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.DO_NOTHING,
    )

    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantidade = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantidade}x {self.produto.nome} - R$ {self.valor}"

    @property
    def valor_total(self) -> Decimal:
        return self.valor * self.quantidade

    class Meta:
        unique_together = [
            ["venda", "produto"],
        ]

        verbose_name = "produto da venda"
        verbose_name_plural = "produtos da venda"


class Lancamento(SoftDeletableModel, TimeStampedModel):
    venda = models.ForeignKey(
        Venda,
        verbose_name="venda",
        on_delete=models.DO_NOTHING,
    )

    tipo = models.SmallIntegerField(default=0, choices=PAGAMENTO_CHOICES)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{PAGAMENTO_CHOICES[self.tipo]} - R$ {self.valor}"

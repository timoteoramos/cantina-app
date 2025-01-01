from django.db import models

from model_utils.models import (
    SoftDeletableModel,
    TimeStampedModel,
)


class Produto(SoftDeletableModel, TimeStampedModel):
    nome = models.CharField(max_length=64)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nome}"

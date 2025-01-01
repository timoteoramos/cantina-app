from django.db import models
from localflavor.br.models import BRCPFField
from phonenumber_field.modelfields import PhoneNumberField

from model_utils.models import (
    SoftDeletableModel,
    TimeStampedModel,
)


class Responsavel(SoftDeletableModel, TimeStampedModel):
    nome = models.CharField(max_length=64)
    telefone = PhoneNumberField()
    cpf = BRCPFField()

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name = "responsável"
        verbose_name_plural = "responsáveis"


class Aluno(SoftDeletableModel, TimeStampedModel):
    responsavel = models.ForeignKey(
        Responsavel, verbose_name="responsável", on_delete=models.DO_NOTHING
    )

    nome = models.CharField(max_length=64)
    telefone = PhoneNumberField(blank=True, null=True)
    cpf = BRCPFField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nome}"

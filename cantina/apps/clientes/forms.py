from django.forms import ModelForm
from localflavor.br.forms import BRCPFField
from phonenumber_field.formfields import SplitPhoneNumberField

from .models import (
    Aluno,
    Responsavel,
)


class AlunoForm(ModelForm):
    cpf = BRCPFField(label="CPF")
    telefone = SplitPhoneNumberField()

    class Meta:
        model = Aluno

        fields = [
            "responsavel",
            "nome",
            "cpf",
            "telefone",
        ]


class ResponsavelForm(ModelForm):
    cpf = BRCPFField(label="CPF")
    telefone = SplitPhoneNumberField()

    class Meta:
        model = Responsavel

        fields = [
            "nome",
            "cpf",
            "telefone",
        ]

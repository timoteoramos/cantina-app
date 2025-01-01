from django.contrib import admin

from .forms import (
    AlunoForm,
    ResponsavelForm,
)

from .models import (
    Aluno,
    Responsavel,
)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm

    list_display = [
        "nome",
    ]

    search_fields = [
        "cpf",
        "nome",
        "telefone",
        "responsavel__cpf",
        "responsavel__nome",
        "responsavel__telefone",
    ]


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    form = ResponsavelForm

    list_display = [
        "nome",
    ]

    search_fields = [
        "cpf",
        "nome",
        "telefone",
    ]

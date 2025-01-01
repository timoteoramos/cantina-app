from django.contrib import admin

from .models import (
    Lancamento,
    Venda,
    VendaProduto,
)


class LancamentoInline(admin.StackedInline):
    extra = 0

    fields = [
        "tipo",
        "valor",
    ]

    model = Lancamento


class VendaProdutoInline(admin.TabularInline):
    extra = 0

    fields = [
        "produto",
        "quantidade",
        "valor",
        "valor_total",
    ]

    model = VendaProduto

    readonly_fields = [
        "valor_total",
    ]


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    date_hierarchy = "created"

    fields = [
        "aluno",
        "total_venda",
        "total_pago",
        "pago",
    ]

    inlines = [
        VendaProdutoInline,
        LancamentoInline,
    ]

    list_display = [
        "aluno__nome",
        "total_venda",
        "total_pago",
        "pago",
    ]

    list_filter = [
        "pago",
    ]

    readonly_fields = [
        "total_venda",
        "total_pago",
        "pago",
    ]

    search_fields = [
        "aluno__cpf",
        "aluno__nome",
        "aluno__telefone",
        "aluno__responsavel__cpf",
        "aluno__responsavel__nome",
        "aluno__responsavel__telefone",
    ]

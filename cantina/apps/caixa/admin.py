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
    ]

    model = VendaProduto


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
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

    readonly_fields = [
        "total_venda",
        "total_pago",
        "pago",
    ]

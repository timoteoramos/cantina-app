from django.contrib import admin

from .models import (
    Lancamento,
    Venda,
    VendaProduto,
)


class LancamentoInline(admin.StackedInline):
    model = Lancamento


class VendaProdutoInline(admin.TabularInline):
    model = VendaProduto


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [
        VendaProdutoInline,
        LancamentoInline,
    ]

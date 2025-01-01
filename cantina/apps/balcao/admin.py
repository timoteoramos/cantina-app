from django.contrib import admin

from .models import (
    Produto,
)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    fields = (
        "nome",
        "valor",
    )

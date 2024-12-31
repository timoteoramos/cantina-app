from django.contrib import admin

from .models import (
    Venda,
)


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    pass

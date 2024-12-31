from django.contrib import admin

from .models import (
    Aluno,
    Responsavel,
)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    pass

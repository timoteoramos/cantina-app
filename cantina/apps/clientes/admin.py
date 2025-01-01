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


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    form = ResponsavelForm

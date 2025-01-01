from django.apps import AppConfig


class CaixaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cantina.apps.caixa"
    verbose_name = "Caixa"

    def ready(self):
        from . import signals

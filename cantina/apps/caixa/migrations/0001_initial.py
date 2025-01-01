# Generated by Django 5.1.4 on 2025-01-01 14:41

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("balcao", "0001_initial"),
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Venda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                ("pago", models.BooleanField(default=False)),
                (
                    "total_venda",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0"), max_digits=8
                    ),
                ),
                (
                    "total_pago",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0"), max_digits=8
                    ),
                ),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="clientes.aluno",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Lancamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                (
                    "tipo",
                    models.SmallIntegerField(
                        choices=[
                            (0, "Dinheiro"),
                            (1, "Débito"),
                            (2, "Crédito"),
                            (3, "Pix"),
                        ],
                        default=0,
                    ),
                ),
                ("valor", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "venda",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="caixa.venda",
                        verbose_name="venda",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VendaProduto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                (
                    "valor",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                ("quantidade", models.SmallIntegerField(default=1)),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="balcao.produto",
                    ),
                ),
                (
                    "venda",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="caixa.venda",
                        verbose_name="venda",
                    ),
                ),
            ],
            options={
                "verbose_name": "produto da venda",
                "verbose_name_plural": "produtos da venda",
                "unique_together": {("venda", "produto")},
            },
        ),
        migrations.AddField(
            model_name="venda",
            name="produtos",
            field=models.ManyToManyField(
                through="caixa.VendaProduto", to="balcao.produto"
            ),
        ),
    ]

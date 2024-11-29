# Generated by Django 4.2.13 on 2024-08-23 14:38

from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps
from django.db.models.functions import Coalesce


def separate_exception_fields(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    DBTaskResult = apps.get_model("django_tasks_database", "DBTaskResult")

    DBTaskResult.objects.using(schema_editor.connection.alias).update(
        exception_class_path=Coalesce(
            models.F("exception_data__exc_type"), models.Value("", models.JSONField())
        ),
        traceback=Coalesce(
            models.F("exception_data__exc_traceback"),
            models.Value("", models.JSONField()),
        ),
    )


class Migration(migrations.Migration):
    dependencies = [
        ("django_tasks_database", "0012_add_separate_exception_fields"),
    ]

    operations = [migrations.RunPython(separate_exception_fields)]
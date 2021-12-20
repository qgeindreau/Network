from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class NotebooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "notebooks"
    verbose_name = _("Notebooks")



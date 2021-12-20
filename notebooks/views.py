from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from helpers import AuthorRequiredMixin
from .models import Notebook
from .forms import NotebookForm


class NotebooksListView(LoginRequiredMixin, ListView):
    """Basic ListView implementation to call the published Notebooks list."""

    model = Notebook
    paginate_by = 15
    context_object_name = "notebooks"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Notebook.objects.get_counted_tags()
        return context

    def get_queryset(self, **kwargs):
        return Notebook.objects.get_published()


class DraftsListView(NotebooksListView):
    """Overriding the original implementation to call the drafts Notebooks
    list."""

    def get_queryset(self, **kwargs):
        return Notebook.objects.get_drafts()


class CreateNotebookView(LoginRequiredMixin, CreateView):
    """Basic CreateView implementation to create new Notebooks."""

    model = Notebook
    message = _("Your Notebook has been created.")
    form_class = NotebookForm
    template_name = "notebooks/notebook_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("notebooks:list")


class EditNotebookView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    """Basic EditView implementation to edit existing Notebooks."""

    model = Notebook
    message = _("Your Notebook has been updated.")
    form_class = NotebookForm
    template_name = "notebooks/notebook_update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("notebooks:list")


class DetailNotebookView(LoginRequiredMixin, DetailView):
    """Basic DetailView implementation to call an individual Notebook."""

    model = Notebook

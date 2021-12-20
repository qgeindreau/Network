from django.urls import re_path

from .views import (
    NotebooksListView,
    DraftsListView,
    CreateNotebookView,
    EditNotebookView,
    DetailNotebookView,
)

app_name = "Notebooks"
urlpatterns = [
    re_path(r"^$", NotebooksListView.as_view(), name="list"),
    re_path(r"^write-new-Notebook/$", CreateNotebookView.as_view(), name="write_new"),
    re_path(r"^drafts/$", DraftsListView.as_view(), name="drafts"),
    re_path(r"^edit/(?P<pk>\d+)/$", EditNotebookView.as_view(), name="edit_notebook"),
    re_path(r"^(?P<slug>[-\w]+)/$", DetailNotebookView.as_view(), name="notebook"),
]

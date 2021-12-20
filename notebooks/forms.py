from django import forms

from markdownx.fields import MarkdownxFormField

from .models import Notebook
from ckeditor.widgets import CKEditorWidget

class NotebookForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    edited = forms.BooleanField(
        widget=forms.HiddenInput(), required=False, initial=False
    )

    class Meta:
        model = Notebook
        fields = ["title", "file","vue","description", "tags", "status", "edited"]
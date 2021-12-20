from django import forms

from markdownx.fields import MarkdownxFormField

from .models import Article
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    edited = forms.BooleanField(
        widget=forms.HiddenInput(), required=False, initial=False
    )
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ["title", "content", "image", "tags", "status", "edited"]
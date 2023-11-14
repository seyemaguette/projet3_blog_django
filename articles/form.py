
from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
class ArticleForm(forms.ModelForm):
    
    title = forms.CharField(
        label = 'Titre',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}))
    summary = forms.CharField(
        label = 'Resumé',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}))
    content = forms.CharField(
        label = 'Contenu de voter blog',
        widget=CKEditorWidget())
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content']
       
       
   
       
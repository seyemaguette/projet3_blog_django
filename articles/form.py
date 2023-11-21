
from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
class ArticleForm(forms.ModelForm):
    
    image = forms.ImageField(
        label = 'Image d"acceuil de votre blog',
        widget=forms.FileInput(
            attrs={
                "class": "form-control"}))
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
        fields = ['image','title', 'summary', 'content']
       
       
   
       
from django import forms
from . models import BlogModel,CommentModel

class BlogForm(forms.ModelForm):
    publication_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = BlogModel
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('content',)
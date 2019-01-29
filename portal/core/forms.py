from django import forms

class SearchNotice(forms.Form):
    title = forms.CharField(label='Título', max_length=100)
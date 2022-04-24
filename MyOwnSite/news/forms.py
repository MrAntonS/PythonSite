from platform import win32_edition
from django import forms
from .models import *


class NewsForms(forms.Form):
    title = forms.CharField(max_length=150, label='Name', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Content', required=False, widget=forms.Textarea(attrs={"class": "form-control",
                                                                                            "rows": 5}))
    is_published = forms.BooleanField(label='Publish', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Choose')


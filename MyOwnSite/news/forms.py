from django import forms
from .models import News


class NewsForms(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = dict(title=forms.TextInput(attrs={"class": "form-control"}), content=forms.Textarea(
            attrs={"class": "form-control", "rows": 5}), category=forms.Select(attrs={'class': 'forms-control'}))
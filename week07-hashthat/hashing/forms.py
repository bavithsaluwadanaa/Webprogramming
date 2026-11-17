from django import forms

class HashForm(forms.Form):
    text = forms.CharField(label="Enter text here:", widget=forms.Textarea(attrs={"rows": 4, "id": "id_text"}))

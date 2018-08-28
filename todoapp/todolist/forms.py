from django import forms

class addtodo(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    created = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    
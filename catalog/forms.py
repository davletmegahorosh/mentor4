from django import forms
from catalog.models import Pizza

class PizzaCreateForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = 'image name price'.split()

class CommentCreate(forms.Form):
    text = forms.CharField()
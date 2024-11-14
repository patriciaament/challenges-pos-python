from django import forms

class EquationForm(forms.Form):
    a = forms.FloatField(label="Valor de a", required=True)
    b = forms.FloatField(label="Valor de b", required=True)
    c = forms.FloatField(label="Valor de c", required=True)
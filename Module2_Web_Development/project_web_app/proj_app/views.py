# segundo_grau/views.py

from django.shortcuts import render
from .form import EquationForm
import math

def index(request):
    resultado = None
    erro = None

    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

        if a == 0:
            erro = "O valor de 'a' deve ser diferente de zero para uma equação do segundo grau."
        else:
            delta = b**2 - 4*a*c

        if delta < 0:
            erro = "A equação não possui raízes reais."
        elif delta == 0:
            raiz = -b / (2 * a)
            resultado = (raiz,)
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            resultado = (raiz1, raiz2)
    else:
        form = EquationForm()

    return render(request, 'url/index.html', {
        'form': form,
        'resultado': resultado,
        'erro': erro
    })

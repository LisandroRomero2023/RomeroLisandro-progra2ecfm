from django.shortcuts import render
import re

# Create your views here.

def editor(request):
    return render(request, 'editor.html')

def analisis(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        patron = re.compile(r'(?:[+-]?\d*\.\d+|[-+]?\d+|if|else|for|while)', re.IGNORECASE)
        matches = patron.findall(text)
        
        textoResaltado = text
        for match in set(matches):
            textoResaltado = re.sub(re.escape(match), f'<span style="color: blue;">{match}</span>', textoResaltado)
        
        textoResaltado = textoResaltado.replace('\n', '<br>')
        
        return render(request, 'result.html', {'highlighted_text': textoResaltado})
    return render(request, 'editor.html')

from django.shortcuts import render, redirect
from .models import Textshearing
from .forms import Shearing
import hashlib


def index(request):
    text = Textshearing.objects.all()
    return render(request, 'index.html', {'text':text})


def texts(request):
    if request.method == 'POST':
        form = Shearing(request.POST)
        if form.is_valid():
            result1 = form.cleaned_data['text']
            result2 = form.cleaned_data['title']
            hashed_value = hashlib.md5(result1.encode()).hexdigest()
            new_url = Textshearing(
                text = result1,
                urls = hashed_value,
                title = result2
            )
            new_url.save()
            return redirect('index')
    else:
        form = Shearing()
    return render(request, 'texts.html', {'form': form}) 


def urls(request, urls):
    x = Textshearing.objects.get(urls=urls)
    return render(request, 'urls.html', {'x':x})


def edit_text(request, urls):
    text = Textshearing.objects.get(urls=urls)
    if request.method == 'POST':
        form = Shearing(request.POST, instance=text)
        if form.is_valid():
            text.title = form.cleaned_data['title']
            text.text = form.cleaned_data['text']
            text.save()
            return redirect('index')
    form=Shearing()
    return render(request, 'edit.html', {'form':form})
    




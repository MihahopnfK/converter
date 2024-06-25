from django.shortcuts import render, redirect
from .models import storage
from .forms import storageForm
from django.views.generic import DetailView
# Create your views here.
def news_home(request):
    news= storage.objects.all()
    return render(request, 'news/news_home.html')
#def create (request):
    #return render(request, 'news/create.html' )

class NewsDetailView(DetailView):
    model = storage
    template_name = 'news/details_view.html'
    context_object_name = 'storage'

def create (request):
    error=''
    if request.method== 'POST':
        form = storageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Неверная форма"

    form = storageForm()
    data = {
        'form':form,
        'error':error,
    }
    return render(request, 'news/create.html',data)
from django.shortcuts import render,redirect
from . models import Movie
from .forms import MovieForms
# Create your views here.
def demo(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request,'index.html',context)

def moviespath(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie = Movie(title=title,description=description,year=year,image=image)
        movie.save()
        return redirect('/')
    return render (request,'add-movie.html')



def update(request,id):
    movie = Movie.objects.get(id = id)
    form = MovieForms(request.POST or None, request.FILES, instance= movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id = id)
        movie.delete()
        return redirect('/')
    
    return render(request,'delete.html')

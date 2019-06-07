from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


# Create your views here.

def home(request):
    return render(request, "index.html", {'title': 'Home Page'})


def contact(request):
    if request.method == 'POST':
        data = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            address=request.POST['address'],
            city=request.POST['city'],
            zipcode=request.POST['zipcode'],
        )
        data.save()
    cnt = Contact.objects.all()

    return render(request, "contact.html", {'title': 'Contact Page', 'rows': cnt})


def about(request):
    return render(request, "about.html", {'title': 'About Page'})


def member(request, cat_id, mem_id):
    return HttpResponse(f"<h1>Team Member ID : {mem_id} from Category ID : {cat_id}</h1>")


def team(request):
    if (request.method == 'GET' and 'cat_id' in request.GET and 'mem_id' in request.GET):
        return HttpResponse(f"<h1>Team Member ID : {request.GET.get('mem_id')} from Category ID : {request.GET.get('cat_id')}</h1>")

    return HttpResponse("<h1>Team Members List</h1>")

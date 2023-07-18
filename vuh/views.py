from django.shortcuts import render

from .models import People

from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        person = people(name=name, school=school, email=email)
        person.save()

        # print(name, school, email)

    return render(request, "home.html")


def people(request):
    d = People.objects.all()

    context = {"data": d}
    return render(request, 'people.html', context)


def delete(request, id):
    dd = People.objects.get(id=id)
    dd.delete()

    return HttpResponse("Delete successful")


def update(request, id):
    l = People.objects.get(id=id)

    return render(request, "edit.html", {"l": l})

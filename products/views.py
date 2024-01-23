# from django.http import HttpResponse
# from django.shortcuts import render
# # внешний вид сайта
#
# def index(request):
#     return HttpResponse("<h1>Hello world</h1>")
# # заголовок
#
# def index(request, users_id, name):
#     return (HttpResponse(f"<p> This user with id:{users_id}, {name}"))
#             #  </p> new str
#
# def about(request):
#     return HttpResponse("Hello world")
#
# def count_age(request, age):
#     if age >=1 and age <= 100:
#         return HttpResponse(f"нормально:{age}")
#     else:
#         return HttpResponse("Так долго не живут")
#
# new_names = ["Ishak", "Nurislam", "Ariet", "Eldar", "Asylbek", "Bek", "Aidana", "Luiza"]
# def find_name(request, name):
#     if name in new_names:
#         return HttpResponse("вы звали этого человека")
#     else:
#         return HttpResponse("вы не звали")
# # h2, h3 уменьшает
#
#
# # aidana123
# #get,post,delete.put- request
# # post создать
# # delete
# # put - класть, изменить




from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Animal


new_names = ["Ishak", "Nurislam", "Ariet", "Eldar", "Asylbek", "Bek", "Aidana", "Luiza"]


def index(request):
    names = {"new_names": new_names}
    return render(request, "index.html", context=names)


hobby = ["Sleeping", "Programming", "Footbal", "Reading", "Volleybal", "Table tennis"]


def about(request):
    list_hobby = {"hooby": hobby}
    return render(request, "about.html", context=list_hobby)


def animal(request):
    animal = Animal.objects.all()
    new_animal = {"new_animal": animal}
    return render(request, "animal2.html", context=new_animal)
# filter(age__lte=2)

def detail_animal(request, animal_name):
    animal = Animal.objects.filter(name=animal_name)
    new_animal = {"new_animal": animal}
    return render(request, "animal.html", context=new_animal)

def delete_animal(request, animal_id):
    animal = Animal.objects.filter(id=animal_id)
    animal.delete()
    return redirect("animal")


def delete_animal_by_name(request, animal_name):
    animal = Animal.objects.filter(name=animal_name)
    animal.delete()
    return redirect("animal")

def create_animal(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        breed = request.POST.get("breed")
        animal = Animal.objects.create(
            name=name,
            age=age,
            breed=breed

        )
    animal.save()
    return redirect("animal")


def edit_animal(request, animal_id):
    animal = Animal.objects.filter(id=animal_id).first()
    new_animal = {"animal": animal}
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        breed = request.POST.get("breed")
        Animal.objects.filter(id=animal_id). update(
            name=name,
            age=age,
            breed=breed
        )
        return redirect("animal")
    return render(request, "edit_animal.html", context=new_animal)

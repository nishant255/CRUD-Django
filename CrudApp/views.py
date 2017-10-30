from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators import csrf

from .forms import PersonForm
from .models import Person


# Create your views here.
def home(request):
    person = Person.objects.all()
    return render(request, 'CrudApp/persons_list.html', {'person': person})


def person_post(request):
    data = dict()
    if request.method == 'POST':
        form = PersonForm()
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = PersonForm()

    context = {'form': form}
    data['html_form'] = render_to_string('CrudApp/persons_create.html', context, request=request)
    return JsonResponse(data)


def get_person(request, pk):
    person = Person.objects.filter(pk=pk)
    person_data = serializers.serialize('json', person)
    return HttpResponse(person_data, content_type="application/json")


@csrf.csrf_exempt
def create_person(request):
    print()
    person = Person(userName=request.POST["user-name"],
                    firstName=request.POST["first-name"],
                    lastName=request.POST["last-name"],
                    email=request.POST["email"],
                    )
    person.save()
    return HttpResponse(status=202)

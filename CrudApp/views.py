from django.shortcuts import render
from .models import Person
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import PersonForm

# Create your views here.
def home(request):
    person = Person.objects.all()
    return render(request, 'CrudApp/persons_list.html', {'person':person})

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


    context = {'form':form}
    data['html_form'] = render_to_string('CrudApp/persons_create.html',context,request=request)
    return JsonResponse(data)





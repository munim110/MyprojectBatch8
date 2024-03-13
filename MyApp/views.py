from django.shortcuts import render
from .models import Contact, Product
from django.http import HttpResponse



# Create your views here.


def hello(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'hello.html', context=context)


def hi(request):
    return render(request, 'page.html')


def single_contact(request, id):
    try:
        contact = Contact.objects.get(pk=id)
        context = {'contact': contact}
        return render(request, 'single_contact.html', context=context)
    except:
        # return all contacts who have Hossain in their name
        contact = Contact.objects.filter(name__icontains='hossain')
        return HttpResponse('404 Not Found')
    

# Model.objects.all() - returns all the objects in the table
# Model.objects.get(pk=id) - returns the object with the primary key id
# Model.objects.filter(field=value) - returns the object with the field value
# Model.objects.first() - returns the first object in the table
# Model.objects.last() - returns the last object in the table
# Model.objects.order_by('field') - returns the objects in the table ordered by the field
# Model.objects.order_by('-field') - returns the objects in the table ordered by the field in descending order
# Model.objects.exclude(field=value) - returns the objects in the table excluding the field value

# details about the filter method
# Model.objects.filter(field=value) - returns the object with the field value
# Model.objects.filter(field__gt=value) - returns the object with the field value greater than value
# Model.objects.filter(field__gte=value) - returns the object with the field value greater than or equal to value
# Model.objects.filter(field__lt=value) - returns the object with the field value less than value
# Model.objects.filter(field__lte=value) - returns the object with the field value less than or equal to value

# Model.objects.filter(field__startswith=value) - returns the object with the field value starting with value
# Model.objects.filter(field__endswith=value) - returns the object with the field value ending with value
# Model.objects.filter(field__icontains=value) - returns the object with the field value containing value in a case insensitive manner
# Model.objects.filter(field__contains=value) - returns the object with the field value containing value in a case sensitive manner
# Model.objects.filter(field__in=[value1, value2]) - returns the object with the field value in the list

# Model.objects.filter(field__range=(value1, value2)) - returns the object with the field value in the range
# Model.objects.filter(field__isnull=True) - returns the object with the field value is null

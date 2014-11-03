from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'I am bod font from the context'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse('Rango says hey there world!\n<a href="/rango/">back to rango</a>')

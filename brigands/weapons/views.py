from django.http import HttpResponse


def index(request):
    return HttpResponse("We will display a table of the weapons here.")
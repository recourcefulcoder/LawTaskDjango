from django.http import HttpResponse


def do_nothing(request):
    return HttpResponse("Hello, world!")

from django.http import HttpResponse, JsonResponse

from .models import Category


def do_nothing(request):
    return HttpResponse("Hello, world!")


def get_documents_metadata(request):
    pass


def get_document_metadata(request, document_id):
    pass


def get_documents(request):
    pass


def get_document(request, document_id):
    pass


def get_category(request):
    parent = request.GET.get("parent")
    dataset = Category.objects.filter(parent=parent).values()
    data = [category for category in dataset]
    return JsonResponse(data, safe=False)

from django.http import HttpResponse

def page1(request):
    return HttpResponse("Hello, this is the first page of contact us.")

def page2(request):
    return HttpResponse("Hello, this is the second page of contact us.")

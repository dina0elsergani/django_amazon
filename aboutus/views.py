from django.http import HttpResponse

def page1(request):
    return HttpResponse("Hello, this is the first page of about us.")

def page2(request):
    return HttpResponse("Hello, this is the second page of about us.")

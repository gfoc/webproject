from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("<b>Welcome to webproject<b/>")

def homepage(request):
    return HttpResponse("Welcome to the Homepage")


def Course(request):
    return HttpResponse("welcometo the course section")


def coursedetails(request,courseid):
    return HttpResponse(courseid)

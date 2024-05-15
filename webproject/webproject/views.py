from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("<b>Welcome to webproject<b/>")

def homepage(request):
    data ={
        'title':'Home Page",
        'about':'This is professional website made for doing specifications and excellaration in different fields',
        'clist':['PHP','JAVA','PYTHON'],
    }

    return render(request,"index.html",data)
    
    return HttpResponse("Welcome to the Homepage")


def Course(request):
    return HttpResponse("welcometo the course section")


def coursedetails(request,courseid):
    return HttpResponse(courseid)

from django.http import HttpResponse
from django.shortcuts import render  #html page ko render karwane ka kaam karega 



def aboutus(request):
    return HttpResponse("<b>Welcome to webproject<b/>")

def homepage(request):
    
    data = {
        'title':'Home..Page',
        'about':'Hello this is a professional website',
        'courselist':['PHP','JAVA','PYTHON'],
        'numbers':[10,20,30,40,50],
        'students_details':[
            {'name':'pradeep','phone':9374838282},
            {'name':'testing','phone':4783384848}
        ]

    }
    return render(request,"index.html",data) 


def Course(request):
    return HttpResponse("welcometo the course section")


def coursedetails(request,courseid):
    return HttpResponse(courseid)


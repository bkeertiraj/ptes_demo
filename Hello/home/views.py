from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1": "god is great",
        "variable2": "i am god"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is Your homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about")
    

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")
    

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is a contact page")
    
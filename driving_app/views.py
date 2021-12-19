from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        return render(request, 'driving_app/index.html')
    else:
        return render(request, 'driving_app/index.html')

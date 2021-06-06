from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")
def register(request):
    return render(request, "register.html")
def frogotpassword(request):
    return render(request, "forgot-password.html")
def charts(request):
    return render(request, "charts.html")
def cards(request):
    return render(request, "cards.html")
def blank(request):
    return render(request, "blank.html")
def now(request):
    return render(request, "404.html")
def buttons(request):
    return render(request, "buttons.html")
def tables(request):
    return render(request, "tables.html")
def ua(request):
    return render(request, "utilities-animation.html")
def ub(request):
    return render(request, "utilities-border.html")
def uc(request):
    return render(request, "utilities-color.html")
def uo(request):
    return render(request, "utilities-other.html")
def grap(request):
    return render(request, "graphql.html")
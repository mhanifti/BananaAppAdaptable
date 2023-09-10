from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'BananaApp',
        'name': 'Muhammad Hanif',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

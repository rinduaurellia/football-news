from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406439002',
        'name': 'Rindu Aurellia Zahra',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
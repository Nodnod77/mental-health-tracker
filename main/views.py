from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406394906 ',
        'name': 'Donia Sakji',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
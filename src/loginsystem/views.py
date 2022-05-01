from django.shortcuts import render
from django.contrib.auth import login
from loginsystem.models import User
from django.http import Http404, JsonResponse
from django.contrib import messages





# Create your views here.


def index(request):
    return render(request, 'landing.html')

def xyz(request):
    return render(request, 'login.html')


def loginuser(request):
    username = request.POST.get('username')
    try:
        user = User.objects.get(username=username)
        return render(request, 'home.html', {'user':user, 'address':user.wallet_address})
    except User.DoesNotExist:
        user = User.objects.create(username=username)
        return render(request, 'home.html', {'user':user})



def autocomplete_user_name(request):
    if 'term' in request.GET:
        user_name = request.GET.get('term')
        user = User.objects.filter(
            username__istartswith=user_name).distinct()
        name = []
        for item_nm in user:
            data = str(item_nm.username)+ ' ' + str(item_nm.wallet_address)
            name.append(data)
        return JsonResponse(name, safe=False)

# def lookup(request, x):
#     user_name = request.GET.get()
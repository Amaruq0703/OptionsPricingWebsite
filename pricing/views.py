from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import json

from .models import *
# Create your views here.

def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "pricing/index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pricing/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "pricing/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "pricing/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "pricing/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pricing/register.html")

def bsm(request):
    return render(request, 'pricing/bsm.html')

def bino(request):
    return render(request, 'pricing/bino.html')

def save_calc(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        stock_price = data.get('S')
        strike_price = data.get('K')
        expiration = data.get('T')
        rfr = data.get('r')
        volatility = data.get('sigma')
        model_type = data.get('model')

        calculation = Calculation(
            user = User.objects.get(pk = request.user.id),
            model = model_type,
            stock = stock_price,
            strike = strike_price,
            expiry = expiration,
            rfr = rfr,
            vol = volatility
        )

        calculation.save()
        return JsonResponse({'status' : 'success'})
    
    return JsonResponse({'status' : 'fail'})

def saved(request):
    user = User.objects.get(pk = request.user.id)
    calcs = Calculation.objects.filter(user = user)
    return render(request, 'pricing/saved.html',{
        'calcs' : calcs
    })

def savedToModel(request, calcID):
    calc = Calculation.objects.get(pk=calcID)
    context = {
        'stock' : calc.stock,
        'strike' : calc.strike,
        'expiry' : calc.expiry,
        'rfr' : calc.rfr,
        'vol' : calc.vol
    }

    model_type = calc.model

    if model_type.lower() == 'black_scholes':
        return render(request, 'pricing/bsm.html', context)
    
    elif model_type.lower() == 'binomial':
        return render(request, 'pricing/bino.html', context)
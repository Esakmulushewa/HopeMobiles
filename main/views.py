from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Screen
from django.db.models import Q
from django.conf import settings
import requests
from django.contrib import messages
# Create your views here.

def home(req):
    screens = Screen.objects.all()
    
    return render(req, "main/home.html", {"screens": screens})

def send_telegram_message(screen, phoneNO, phone_url=None):
    text = (
        f"​🟢ኣዲስ ትእዛዝ!🟢 \n"
        f"📱 የስልክ ኣይነት: {screen.phone_name} \n"
        f"💲 ዋጋ: {screen.price} \n"
        f"📞 የስልክ ቁጥር: {phoneNO} \n"
    )
    if phone_url:
        text += f"Link: {phone_url}"
    url= f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
    })

def types(request, phone_type):
    # type = get_object_or_404(Screen, type__iexact=phone_type)
    # query = request.GET.get("query") or request.GET.get("query", "")
    screens = Screen.objects.filter(type__iexact=phone_type)
    return render(request, 'main/types.html', {
        'screens': screens, 'type': phone_type
    })

def screens(request):
    samsungScreens = Screen.objects.filter(type__iexact="samsung")
    iPhoneScreens = Screen.objects.filter(type__iexact="iphone")
    return render(request, 'main/screens.html', {"samsungScreens": samsungScreens, "iPhoneScreens": iPhoneScreens})

def details(request, screen_id):
    screen = get_object_or_404(Screen, id=screen_id)
    if request.method == "POST":
        phoneNO = request.POST.get("phone")
        phone_url = request.build_absolute_uri(f"/screens/{screen.id}")
        send_telegram_message(screen, phoneNO, phone_url)
        messages.success(request, "ትዕዛዝዎን ተቀብለናል። ባለሞያዎቻችን ከትንሽ ደቂቃዎች በኋላ ይደውሉሎታል።")
        return redirect("home")
    return render(request, 'main/details.html', {
        'screen': screen
    })

def results(request):
    query = request.POST.get("query") or request.GET.get("query", "")
    searches = (Screen.objects.filter(Q(phone_name__icontains=query) | Q(type__icontains=query)))
    
    return render(request, 'main/results.html', {"results": searches, "query": query})


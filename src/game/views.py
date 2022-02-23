import random
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'game/index.html', {})

def play(request):
    word = get_word()
    length = len(word) + 1

    context = {
      'word_range': range(1, length),
      'range': range(1, length + 1)
    }

    return render(request, 'game/play.html', context)

def check(request):
    word = get_word()

    request.POST._mutable = True
    request.POST.pop("guess")
    request.POST.pop("csrfmiddlewaretoken")
    request.POST._mutable = False

    data = {}
    for position, value in request.POST.items():
        idx = int(position) - 1
        if word[idx] == value.upper():
            data[position] = "perfect"
            word = word.replace(value.upper(), " ", 1)
        elif value.upper() in word:
            data[position] = "correct"
            word = word.replace(value.upper(), " ", 1)
        else:
            data[position] = "wrong"

    return JsonResponse(data)

def get_word():
    return "FORUM"

def qr():
    code = str(random.randint(0, 999999))
    padded_code = code.zfill(6)
        
    factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make(padded_code, image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)

    return JsonResponse({ "svg": stream.getvalue().decode() })
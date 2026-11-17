import hashlib
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import HashForm
from .models import HashRecord

def make_digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def home(request):
    if request.method == "POST":
        form = HashForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            digest = make_digest(text)
            HashRecord.objects.get_or_create(digest=digest, defaults={"text": text})
            return redirect("hashing:result", digest=digest)
    else:
        form = HashForm()
    return render(request, "hashing/home.html", {"form": form})

def result(request, digest):
    record = get_object_or_404(HashRecord, digest=digest)
    return render(request, "hashing/result.html", {"record": record})

def quick_hash(request):
    text = request.GET.get("text", "")
    return JsonResponse({"hash": make_digest(text)})

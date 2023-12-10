from django.shortcuts import render
from .models import Picture
from .forms import PictureForm

# Create your views here.
def main(request):
    # mapped to app_instagram/template/...
    return render(request, "app_instagram/index.html", context={"title":"Hello world new instagram"})

def upload(request):
    form = PictureForm(instance=Picture())
    return render(request, "app_instagram/upload.html", context={"title":"Hello world from upload", "form": form})

def pictures(request):
    return render(request, "app_instagram/pictures.html", context={"title":"Hello world from pictures"})

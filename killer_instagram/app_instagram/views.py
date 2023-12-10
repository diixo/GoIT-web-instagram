from django.shortcuts import render

# Create your views here.
def main(request):
    # mapped to app_instagram/template/...
    return render(request, "app_instagram/index.html", context={"title":"Hello world new instagram"})

def upload(request):
    return render(request, "app_instagram/upload.html", context={"title":"Hello world from upload"})

def pictures(request):
    return render(request, "app_instagram/pictures.html", context={"title":"Hello world from pictures"})

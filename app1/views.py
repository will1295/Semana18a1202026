from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def visitar(request):
    visitas = request.session.get("visitas",0)+1
    request.session["visitas"] = visitas
    return HttpResponse(f"Esta pagina ha sido vista {visitas} veces")

def guardar_usuario(request,nombre):
    request.session["usuario_temporal"]=nombre
    return JsonResponse({"guardado":nombre})

def ver_sesion(request):
    return JsonResponse({
        "visitas":request.session.get("visitas",0),
        "usuario_temporal":request.session.get("usuario_temporal"),
    })

def limpiar_session(request):
    request.session.flush()
    return HttpResponse("Datos de sesion eliminados")

def registro_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("inicio")
    else:
            form = UserCreationForm()
    return render(request,"registro.html",{"form":form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            next_url = request.POST.get("next") or request.GET.get("next")
            return redirect(next_url or "inicio")
    else:
            form = AuthenticationForm(request)
    return render(request,"login.html",{"form":form})

@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def inicio_view(request):
    return render(request,"inicio.html",{"usuario":request.user})
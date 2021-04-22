from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def formulario(request):
	return render(request, 'app/formulario.html')

def resultados(request):
	nombre = request.POST['Nombre']
	apellido = request.POST['Apellido']
	number = request.POST['inputNumber']
	email = request.POST['inputEmail']
	radios = request.POST['Dieta']
	select = request.POST['inputSelect']
	checkbox = request.POST.getlist('inputCheck')

	contexto={}
	contexto['nombre'] = nombre
	contexto['apellido'] = apellido
	contexto['number'] = number
	contexto['email'] = email
	contexto['radios'] = radios
	contexto['select'] = select
	contexto['checkbox'] = checkbox

	return render(request, 'app/resultados.html', contexto)

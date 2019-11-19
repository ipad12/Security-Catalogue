from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Generic
from .models import Solution

# Create your views here.
def index(request):
	generic_list = Generic.objects.order_by('-generic_name')[:10]
	solution_list= Solution.objects.order_by('-solution_name')[:9]
	context = {
		'generic_list': generic_list,
		'solution_list': solution_list,
	}
	return render(request, 'home/index.html', context)

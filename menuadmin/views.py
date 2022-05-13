from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# api response if completing in react
def get_items(request):
	items = []

	# not using JsonResponse because I don't feel like writing a serializer
	[items.append(
		{
			'name':x.name,
			'price':float(x.price),
			'description':x.description
		}
		) for x in MenuItem.objects.all()]

	return HttpResponse([items])

def index(request):
	items = []

	# not using JsonResponse because I don't feel like writing a serializer
	[items.append(
		{
			'name':x.name,
			'price':float(x.price),
			'description':x.description
		}
		) for x in MenuItem.objects.all()]

	context = {'items': items}

	return HttpResponse(render(request, 'items.html', context))
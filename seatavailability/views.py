# seatavailability/views.py
from django.http import JsonResponse
# from .models import SeatAvailability
from django.shortcuts import render

# seatavailability/views.py
from django.http import JsonResponse
from .models import Branch

def seat_availability_view(request):
    branches = Branch.objects.all().prefetch_related('categories')
    data = {}

    for branch in branches:
        categories = branch.categories.all().values('name', 'availability')
        data[branch.name] = list(categories)

    return JsonResponse(data)


def index_view(request):
    return render(request, 'index.html')

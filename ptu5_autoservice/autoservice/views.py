from django.shortcuts import render
from django.http import HttpResponse
from . models import Car, Order, Service, CarModel, OrderLine

def index(request):
    # return HttpResponse("Welcome!")
    car_count = Car.objects.count()
    car_model_count = CarModel.objects.count()
    order_line_count = OrderLine.objects.count()
    order_count = Order.objects.count()

    context = {
        'car_count': car_count,
        'car_model_count': car_model_count,
        'order_line_count': order_line_count,
        'order_count': order_count,
        'service_count': Service.objects.count()
    }
    
    return render(request, 'autoservice/index.html', context=context)

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . models import Car, Order, Service, CarModel, OrderLine

def index(request):
    # return HttpResponse("Welcome!")
    car_count = Car.objects.count()
    car_model_count = CarModel.objects.count()
    order_line_count = OrderLine.objects.count()
    order_count = Order.objects.count()
    visits_count = request.session.get('visits_count', 1)
    request.session['visits_count'] = visits_count+1

    context = {
        'car_count': car_count,
        'car_model_count': car_model_count,
        'order_line_count': order_line_count,
        'order_count': order_count,
        'service_count': Service.objects.count(),
        'visits_count': visits_count,
    }
    
    return render(request, 'autoservice/index.html', context=context)

def cars(request):
    return render(request, 'autoservice/cars.html', {'cars': Car.objects.all()})

def car_info(request, car_id):
    return render(request, 'autoservice/car_info.html', {'car': get_object_or_404(Car, id=car_id)})



class OrderListView(ListView):
    model = Order
    # paginate_by = 1
    template_name = 'autoservice/order_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders_count'] = self.get_queryset().count()
        return context


class OrderDetailView(DetailView):
    model = OrderLine
    template_name = 'autoservice/order_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        order_id = self.request.GET.get('order_id')
        if order_id:
            queryset = queryset.filter(order__id=order_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['books_count'] = Book.objects.count()
        context['services_count'] = self.get_queryset().count()
        order_id = self.request.GET.get('order_id')
        context['orders'] = Order.objects.all()
        if order_id:
            context['genre'] = get_object_or_404(Order, id=order_id)
        return context

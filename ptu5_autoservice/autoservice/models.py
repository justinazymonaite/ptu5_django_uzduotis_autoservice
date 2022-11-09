from django.db import models
from datetime import date

class CarModel(models.Model):
    YEAR_CHOICES = ((year, str(year)) for year in reversed(range(1899, date.today().year+1)))
    make = models.CharField('make', max_length=50)
    model = models.CharField('model', max_length=50)
    year = models.IntegerField('year', choices=YEAR_CHOICES)
    engine = models.CharField('engine', max_length=50)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}), {self.engine}"

    class Meta:
        ordering = ['make']
        verbose_name = 'Car model'
        verbose_name_plural = 'Car models'


class Service(models.Model):
    title = models.CharField('title', max_length=50)
    price = models.DecimalField('price', max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.title}: {self.price}"

    class Meta:
        ordering = ['title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Car(models.Model):
    license_plate_number = models.CharField('license plate number', max_length=10)
    vin_code = models.CharField('vin code', max_length=17)
    client = models.CharField('client name', max_length=200)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='car model', related_name='cars')

    def __str__(self) -> str:
        return f"{self.car_model.make} {self.car_model.model} {self.license_plate_number}, {self.vin_code}, {self.client}"

    def display_car_model(self) -> str:
        return ', '.join(car_model.make for car_model in self.car_model.all())
    display_car_model.short_description = 'car model(s)'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars' 


class Order(models.Model):
    order_date = models.DateTimeField('order date', auto_now_add=True, editable=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField('total amount', max_digits=18, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f" {self.car}: {self.total_amount}, {self.order_date}"

    def display_car(self) -> str:
        return ', '.join(car.license_plate_number for car in self.car.all())
    display_car.short_description = 'car(s)'

    def get_total(self):
        total = 0
        for line in self.order_lines.all():
            total += line.total
        return total
    
    def save(self, *args, **kwargs):
        self.total = self.get_total()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order_date'] 
        verbose_name = 'Order'
        verbose_name_plural = 'Orders' 


class OrderLine(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='service', related_name='order_lines')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='order', related_name='order_lines')
    amount = models.IntegerField('amount', default=1)
    price = models.DecimalField('price', max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f" {self.service.title}: {self.amount} x {self.price}"

    @property
    def total(self):
        return self.amount * self.price
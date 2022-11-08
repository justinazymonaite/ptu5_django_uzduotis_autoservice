from django.db import models


class CarModel(models.Model):
    make = models.CharField('make', max_length=200, help_text="Enter the name of car make")
    model = models.CharField('model', max_length=200, help_text="Enter the name of car model")

    def __str__(self):
        return f"({self.make} {self.model})"


class Service(models.Model):
    title = models.CharField('title', max_length=200, help_text="Enter the title of service")
    price = models.DecimalField('price', max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.title}: {self.price}"

    class Meta:
        ordering = ['title', 'price']


class Car(models.Model):
    license_plate_number = models.CharField('license plate number', max_length=20)
    vin_code = models.CharField('vin code', max_length=17)
    client = models.CharField('client', max_length=250)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f" {self.license_plate_number} {self.car_model}, {self.client}"


class Order(models.Model):
    order_date = models.DateTimeField('order date', auto_now_add=True, editable=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    total_amount = models.DecimalField('total amount', max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f" {self.car}, {self.total_amount}"

    class Meta:
        ordering = ['order_date']  

class OrderLine(models.Model):
    service = models.ManyToManyField(Service, help_text="Choose service(s) for the car", verbose_name="service(s)")
    order = models.ManyToManyField(Order)
    amount = models.IntegerField('amount')
    price = models.DecimalField('price', max_digits=18, decimal_places=2)



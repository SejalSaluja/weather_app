from django.db import models

# Create your models here.

class CityWeather(models.Model):
    city = models.TextField()
    country_code = models.TextField()
    temp = models.DecimalField(max_digits = 10, decimal_places = 2)
    pressure = models.DecimalField(max_digits = 10, decimal_places = 2)
    humidity= models.DecimalField(max_digits = 10, decimal_places = 2)
    timestamp = models.DateTimeField(auto_now_add = True)

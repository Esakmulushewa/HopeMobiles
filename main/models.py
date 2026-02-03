from django.db import models
# Create your models here.
#     
class Screen(models.Model):
    type = models.CharField(max_length=50, default="")
    phone_name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='screens/')

    def __str__(self):
        return self.phone_name

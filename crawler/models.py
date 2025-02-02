from django.db import models
from django.core.exceptions import ValidationError


def validate_hour(hour):
    if hour < 0 or 23 < hour:
        raise ValidationError(
            ("%(value)s is not among 0-23"),
            params={"value": hour},
        )

class Seller(models.Model):
    seller = models.CharField(max_length=50)

    def __str__(self): 
        return self.seller 

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=50)
    product_name = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=17)
    seller = models.ForeignKey(Seller, on_delete=models.RESTRICT)
    time = models.IntegerField(
        choices=[
            ("0", 0),
            ("1", 1),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("11", 11),
            ("12", 12),
            ("13", 13),
            ("14", 14),
            ("15", 15),
            ("16", 16),
            ("17", 17),
            ("18", 18),
            ("19", 19),
            ("20", 20),
            ("21", 21),
            ("22", 22),
            ("23", 23),
        ],
        validators=[validate_hour]
    )

    class Meta:
        unique_together = ('sku','time')
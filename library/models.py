from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField(default = 1)
    last_update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class Customers(models.Model):
    ROLE = (("student", "S"), ("teacher", "T"))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE, default="student")


class BookRecord(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    returned_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_created=True)

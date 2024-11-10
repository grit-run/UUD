from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    orders = models.ManyToManyField("Order", through="OrderUser", related_name="users")


class UserAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    zipcode = models.CharField(max_length=6)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    users = models.ManyToManyField(User, through=UserAddress, related_name="addresses")


class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    price = models.FloatField()


class OrderUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_cost = models.FloatField()


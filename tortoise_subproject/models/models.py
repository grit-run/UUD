from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    name = fields.CharField(max_length=100)
    surname = fields.CharField(max_length=100)
    age = fields.IntField()
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
#    addresses = fields.ManyToManyField("Address", through="UserAddress", related_name="users")

    class Meta:
        table = "users"

    def __str__(self):
        return self.username


class UserAddress(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="addresses")
    address = fields.ForeignKeyField("models.Address", related_name="users")

    class Meta:
        table = "user_addresses"

    def __str__(self):
        return self.user.username


class Address(Model):
    id = fields.IntField(pk=True)
    zipcode = fields.CharField(max_length=6)
    street = fields.CharField(max_length=100)
    number = fields.CharField(max_length=100)
    apartment = fields.CharField(max_length=100)
    city = fields.CharField(max_length=100)
    country = fields.CharField(max_length=100)
#    users = fields.ManyToManyField("models.User", through="UserAddress", related_name="addresses")

    class Meta:
        table = "addresses"

    def __str__(self):
        return self.city


class Group(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)

    class Meta:
        table = "groups"

    def __str__(self):
        return self.name


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    group = fields.ForeignKeyField("models.Group", related_name="products")
    description = fields.CharField(max_length=100)
    price = fields.FloatField()

    class Meta:
        table = "products"

    def __str__(self):
        return self.name


class OrderUser(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="orders")
    order = fields.ForeignKeyField("models.Order", related_name="users")

    class Meta:
        table = "order_users"

    def __str__(self):
        return self.order


class Order(Model):
    id = fields.IntField(pk=True)
#    user = fields.ForeignKeyField("models.User", related_name="orders", on_delete="CASCADE")
    product = fields.ForeignKeyField("models.Product", related_name="orders", on_delete="CASCADE")
    quantity = fields.IntField()
    total_cost = fields.FloatField()

    class Meta:
        table = "orders"

    def __str__(self):
        return self.total_cost

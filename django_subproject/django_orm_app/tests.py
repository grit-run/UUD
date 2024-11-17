import time
from django.test import TestCase
from .models import *


def test_running_time(operation, run_time):
    """ write run time to file """
    with open('run_time.txt', 'a') as file:
        file.write(('{0}: {1}\n').format(operation, run_time))


class OrmAppTestCase(TestCase):
    def dj_test_create(self):
        """ Create USers/Addresses/Products"""
        start_time = time.time()  # start time of test

        for i in range(1000):
            user = User(
                username="AnyUser_{}".format(i),
                name="J{}".format(i),
                surname="Doo_{}".format(i),
                age=i if i < 100 else 30 and 40 if i < 500 else 50,
                email="{}@{}.tst".format(User.name, User.surname),  #
                password="password_{}".format(i)
            )
            user.save()

        for i in range(1000):
            address = Address(
                zipcode="12345",
                street="Street_{}".format(i),
                number="1234",
                apartment="Apt_{}".format(i),
                city="City_{}".format(i),
                country="Country"
            )
            address.save()

        for i in range(5):
            group = Group(name="Group_for_product_{}".format(i))
            group.save()

        for i in range(10000):
            product = Product(
                name="Product_{}".format(i),
                group=Group(name="Group_{}".format(i if i < 5 else 3)),
                description="Description_{}".format(i),
                price=i
            )
            product.save()

        self.assertEqual(User.objects.count(), 1000)
        self.assertEqual(Address.objects.count(), 1000)
        self.assertEqual(Product.objects.count(), 10000)
        self.assertEqual(Group.objects.count(), 5)

        end_time = time.time()  # end time of test
        run_time=end_time - start_time
        test_running_time('django orm app create', run_time)
        return run_time

    def dj_test_read(self):
        """ Read USers/Addresses/Products"""
        start_time = time.time()  # start time of test
        for i in range(1000):
            User.objects.get(id=i)

        for i in range(1000):
            Address.objects.get(id=i)

        for i in range(10000):
            Product.objects.get(id=i)

        for i in range(5):
            Group.objects.get(id=i)

        end_time = time.time()  # end time of test
        run_time=end_time - start_time
        test_running_time('django orm app read', run_time)
        return run_time

    def dj_test_update(self):
        """ Update USers/Adresses/Products"""
        start_time = time.time()  # start time of test
        for i in range(1000):
            User.objects.get(id=i).name = "J{}".format(i)
            User.objects.get(id=i).save()
        end_time = time.time()  # end time of test
        run_time=end_time - start_time
        test_running_time('django orm app update', run_time)
        return run_time

    def dj_test_delete(self):
        """ Delete USers/Adresses/Products"""
        start_time = time.time()  # start time of test
        for i in range(1000):
            User.objects.get(id=i).delete()
        end_time = time.time()  # end time of test
        run_time=end_time - start_time
        test_running_time('django orm app delete', run_time)
        return run_time



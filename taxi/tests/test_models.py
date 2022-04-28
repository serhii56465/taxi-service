from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer_ = Manufacturer.objects.create(name="BMW", country="Ukraine")

        self.assertEqual(str(manufacturer_), f"{manufacturer_.name} {manufacturer_.country}")

    def test_driver_str(self):
        driver_ = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="test first",
            last_name="test last"
        )

        self.assertEqual(str(driver_), f"{driver_.username} ({driver_.first_name} {driver_.last_name})")

    def test_car_str(self):
        manufacturer_ = Manufacturer.objects.create(name="BMW", country="Ukraine")
        car_ = Car.objects.create(model="Mercedes", manufacturer=manufacturer_)

        self.assertEqual(str(car_), car_.model)

    def test_create_driver_with_license(self):
        username = "test"
        password = "test1234"
        license_number = "kkk2222"
        driver_ = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number
        )

        self.assertEqual(driver_.username, username)
        self.assertTrue(driver_.check_password(password))
        self.assertEqual(driver_.license_number, license_number)


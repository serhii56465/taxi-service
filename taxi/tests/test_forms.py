from django.test import TestCase

from taxi.forms import DriverUserCreationForm


class FormsTests(TestCase):
    def test_driver_creation_with_license_first_name_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "test first",
            "last_name": "test last",
            "license_number": "SSS3333"
        }
        form = DriverUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
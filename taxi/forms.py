from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from taxi.models import Driver, Car


class DriverForm(forms.ModelForm):
    MIN_LICENSE_CHARACTERS = 8

    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != DriverForm.MIN_LICENSE_CHARACTERS:
            raise ValidationError(f"License has to consist only {DriverForm.MIN_LICENSE_CHARACTERS}")

        if not license_number[:3].isupper() or not license_number[:3].isalpha():
            raise ValidationError("The first 3 characters have to be UpperCase")

        if license_number[-5:].isdigit() is False:
            raise ValidationError("The last 5 characters have to be digit")

        return license_number


class DriverUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number", "first_name", "last_name")


class CarForms(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"


class CarSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by model..."}),
    )


class DriverSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by License number..."}),
    )


class ManufacturerSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."}),
    )

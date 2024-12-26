from django import forms
from django.contrib.auth.forms import User

from django.contrib.auth.password_validation import password_changed
from django.db.models.fields import return_None


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(required=True)
    # age = forms.IntegerField()
    # image = forms.ImageField()


    class Meta:
        model = User
        fields = ["username", "password", "password_confirm"]

    def clean (self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password")
        if (password and password_confirm) and (password != password_confirm):
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data

class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
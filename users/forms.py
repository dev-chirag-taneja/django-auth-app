from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError  


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True, validators=[EmailValidator])  

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        # check for existing email
        if User.objects.filter(email=cleaned_data["email"]).exists():
            raise ValidationError("User with this email already exists!")
        return self.cleaned_data
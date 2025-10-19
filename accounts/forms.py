from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="email format: ******@gmail.com "
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Enter your desired username'}
        )
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Enter your email address'}
        )
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Enter a strong password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm your password'}
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use. Please use a different one.")
            
        return email


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Enter your email address'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Enter your password'}
        )

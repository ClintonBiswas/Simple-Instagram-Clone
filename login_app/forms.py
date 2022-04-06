from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from login_app.models import userProfile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True,label="",
    widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    username = forms.CharField(required=True,label="",
    widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password1 = forms.CharField(required=True,label="",
    widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(required=True,label="",
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )
    class meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class profileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ('name', 'profile_pic', 'bio_data', 'social_site')

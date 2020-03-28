from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ('username', 'password')
        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control'}),

        }


team_choice = (
    ('Flutter Application Developement'),
    ('Django Web Developement')
)


class ProfileInfoForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta():
        model = UserProfileInfo
        fields = ('fname', 'lname', 'email', 'contact', 'portfolio', 'profile_pic', 'team')
        team = forms.CharField(widget=forms.Select(choices=team_choice))
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-inline form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-inline form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'portfolio': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.TextInput(attrs={'class': 'btn btn-warning dropdown-toggle', 'placeholder': 'Select'})

        }

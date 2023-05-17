from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150, required=True)
    password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput)

    
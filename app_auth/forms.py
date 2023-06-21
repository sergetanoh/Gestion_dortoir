from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="nom utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))


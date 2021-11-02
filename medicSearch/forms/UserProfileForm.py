from django import forms
from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.models import User
from medicSearch.models.Profile import Profile


class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:
            del self.fields['role']
    
    class Meta:
        model = Profile
        fields = ('user', 'role', 'birthday', 'image') #pontos que seram usados, usar __all__ se for todos ou exclude para excluir algum em especifico

        widgets = {
            'user': forms.HiddenInput(),
            'role': forms.Select(attrs={'class': "form-control"}),
            'birthday': forms.DateInput(attrs={'class': "form-control", "type": "date"}),
            'image': forms.FileInput(attrs={'class':"form-control"})
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"})
        }

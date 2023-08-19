from django import forms

from client.models import Client


class ClientForms(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
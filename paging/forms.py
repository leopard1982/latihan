from django import forms
from .models import DaftarNama

class InputDaftarNama(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = DaftarNama

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),

        }
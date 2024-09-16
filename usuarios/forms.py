from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),  # Usa un selector de fechas
        input_formats=['%Y-%m-%d'],  # Especifica el formato de fecha esperado
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'fecha_nacimiento']
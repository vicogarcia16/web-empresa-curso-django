from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre", min_length=3, max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Escriba su nombre',
                                      'class': 'form-control'}))
    email = forms.EmailField(
        label="Email", min_length=3, max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Escriba su email',
                                      'class': 'form-control'}))
    content = forms.CharField(
        label="Contenido", min_length=10, max_length=1000, required=True, 
        widget=forms.Textarea(attrs={'placeholder': 'Escriba su mensaje',
                                      'rows': 3, 'class': 'form-control'}))
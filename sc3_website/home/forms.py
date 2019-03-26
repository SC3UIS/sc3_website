from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',
                'id':
                    'name',
                'placeholder':
                    'Su nombre *',
                'required':
                    "required",
                'data-validation-required-message':
                    "Por favor, ingrese su nombre."
            }))

    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',
                'id':
                    'email',
                'type':
                    'email',
                'placeholder':
                    'Su correo *',
                'required':
                    "required",
                'data-validation-required-message':
                    "Por favor, ingrese su correo."
            }))

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':
                    'form-control',
                'id':
                    'message',
                'placeholder':
                    'Su mensaje *',
                'required':
                    "required",
                'data-validation-required-message':
                    "Por favor, ingrese su mensaje."
            }))

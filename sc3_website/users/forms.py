from django import forms
from .models import Project, ResearchArea
from bootstrap_datepicker_plus import DatePickerInput

import datetime


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'tech_reqs',
            'institution',
            'init_date',
            'end_date',
            'responsible',
            'responsible_email',
            'num_accounts',
            'project_type',
            'cost',
            'coie_percent',
            'research_area',
        ]

    title = forms.CharField(
        label='Título',
        widget=forms.TextInput(attrs={
            'placeholder': 'Título del proyecto.',
            'class': 'form-control',
        }))

    description = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Descripción del proyecto.',
                'class': 'form-control',
                'rows': 2,
            }))

    tech_reqs = forms.CharField(
        label='Req. Técnicos',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Hardware y Software (si aplica).',
                'class': 'form-control',
                'rows': 2,
            }),
    )

    institution = forms.CharField(
        label='Institución',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Laboratorio, Escuela, Facultad o Institución.',
                'class': 'form-control',
            }))

    init_date = forms.DateField(
        label='Fechas',
        input_formats=['%d/%m/%Y'],
        widget=DatePickerInput(
            attrs={
                'placeholder': 'Inicio.',
            },
            options={
                'minDate': (datetime.datetime.today() +
                            datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                'format':
                    'DD/MM/YYYY',
                'useCurrent':
                    False,
                'showTodayButton':
                    False,
                'showClear':
                    False,
                'showClose':
                    False
            },
        ))

    end_date = forms.DateField(
        #label = 'Fecha de finalización:',
        input_formats=['%d/%m/%Y'],
        widget=DatePickerInput(
            attrs={'placeholder': 'Final.'}, options={'format': 'DD/MM/YYYY'}))

    responsible = forms.CharField(
        label='Responsable',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Profesor/Investigador encargado.',
                'class': 'form-control'
            }))

    responsible_email = forms.EmailField(
        label='Correo de contacto',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ejemplo@dominio.com',
            'class': 'form-control'
        }))

    num_accounts = forms.IntegerField(
        label='Cuentas de usuario',
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Número requerido.',
                'class': 'form-control',
                'type': 'number'
            }))

    # TODO: Poner como enlace de info apuntando a documentación de servicios y costos
    # (Consultar Detalles de Los Servicios y Costos)
    project_type = forms.ChoiceField(
        label='Tipo de proyecto',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=Project.project_type_choices)

    cost = forms.DecimalField(
        label='Costo del proyecto',
        widget=forms.TextInput(
            attrs={
                'placeholder': '(Pesos)',
                'readonly': 'true',
                'class': 'form-control',
                'type': 'number'
            }))

    coie_percent = forms.DecimalField(
        label='Financiamiento solicitado al COIE',
        min_value=0,
        max_value=100,
        initial=0,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    research_area = forms.ModelChoiceField(
        label='Área de investigación',
        queryset=ResearchArea.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

from django import forms
from .models import Project
from bootstrap_datepicker_plus import DatePickerInput

import datetime

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','tech_reqs',
              'institution','init_date',
              'end_date','responsible','responsible_email',
              'num_accounts','project_type','cost',
              'research_area']

    title = forms.CharField(
        label='Título:',
        widget=forms.TextInput(attrs={'class':'form-control'})
        )

    description = forms.CharField(
        label='Descripción',
        widget = forms.Textarea(attrs={'class':'form-control', 'rows':2})
        )

    tech_reqs = forms.CharField(
        label='Requisitos Técnicos: Hardware y Software (si aplica)',
        widget = forms.Textarea(attrs={'class':'form-control', 'rows':2})
        )

    institution = forms.CharField(
        label = 'Institución',
        widget=forms.TextInput(attrs={'class':'form-control'})
        )

    init_date = forms.DateField(
        label = 'Fecha de inicio:',
        widget = DatePickerInput(
            options={
                'minDate': (datetime.datetime.today() + 
                            datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                'format':'DD/MM/YYYY',
                'showTodayButton':False,
                'showClear': False,
                'showClose': False
                }
            )
        )

    end_date = forms.DateField(
        label = 'Fecha de finalización:',
        widget = DatePickerInput(
            options={
                'minDate': (datetime.datetime.today() + 
                        datetime.timedelta(days=91)).strftime('%Y-%m-%d'),
                'format':'DD/MM/YYYY'
                }
            )
        )

    responsible = forms.CharField(
        label = 'Nombre completo del Profesor/Investigador encargado:',
        widget=forms.TextInput(attrs={'class':'form-control'})
        )

    responsible_email = forms.EmailField(
        label = 'Correo de contacto para el proyecto:',
        widget = forms.EmailInput(attrs={'class':'form-control'})
        )

    num_accounts = forms.IntegerField(
        label = 'Número de cuentas de usuario requeridas:',
        widget=forms.TextInput(attrs={'class':'form-control'})
        )

    project_type = forms.ChoiceField(
        label = 'Tipo de proyecto: (Consultar Detalles de Los Servicios y Costos)',
        widget=forms.Select(attrs={'class':'form-control'}),
        choices=Project.project_type_choices
        )
    
    cost = forms.DecimalField(
        label = 'Costo del proyecto (pesos):',
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    
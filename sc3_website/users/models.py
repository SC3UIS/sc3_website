from django.db import models

class ResearchArea(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    tech_reqs = models.TextField(blank=True, null=True)

    status_choices = (
        ('active', 'Active'),
        ('ended', 'Ended'),
        ('rejected', 'Rejected')
    )
    status = models.CharField(
        max_length=10,
        verbose_name = 'Estado del Proyecto',
        choices = status_choices,
        default = 'active')

    institution = models.CharField(max_length=100)
    init_date = models.DateField()
    end_date = models.DateField()
    responsible = models.CharField(max_length=100)
    responsible_email = models.CharField(max_length=100)
    num_accounts = models.IntegerField()

    project_type_choices = (
        ('','Seleccione el tipo de projecto'),
        ('uis', 'UIS'),
        ('external', 'Externo')
    )
    project_type = models.CharField(
        max_length=10,
        choices = project_type_choices,
    )

    cost = models.FloatField(default=0)
    coie_percent = models.FloatField(default=0)
    renew_date = models.DateField(null=True)
    research_area = models.ForeignKey(ResearchArea, on_delete=models.CASCADE)
    

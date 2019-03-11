from django.contrib import admin
from .models import Project, ResearchArea

class ProjectInline(admin.StackedInline):
    model = Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title','responsible',
                    'responsible_email','init_date',
                    'end_date','research_area')
    list_display_links = ('id','title',
                          'responsible','responsible_email',
                          'init_date','end_date')
    search_fields = ('title','responsible')

class ResearchAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [ProjectInline,]





# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(ResearchArea, ResearchAreaAdmin)

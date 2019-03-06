from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProjectList.as_view(), name='project_list'),
    url(r'^project/<int:pk>', views.ProjectView.as_view(), name='project_view'),
    url(r'^project/new', views.ProjectCreate.as_view(), name='project_new'),
]
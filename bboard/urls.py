from django.urls import path
from . import views


app_name = 'bboard'

urlpatterns = [
path ('rubrics/<int:rubric_id>/', views.by_rubric, name='by_rubric'),
path('', views.index, name='index'),
path('json/', views.data_json, name='data_json'),
path('rubric-json/', views.rubricsJson, name='rubrics_json')


]



from django.urls import path
from .views import index, by_rubric
from bboard import views
urlpatterns = [
path ('<int:rubric_id>/', by_rubric, name='by_rubric'),
path('', index, name='index'),
path('json', views.json, name='json')

]

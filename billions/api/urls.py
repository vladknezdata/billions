from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name='api'),
    path('reference-list/', views.referenceList, name='reference-list'),
    path('reference-detail/<str:pk>/', views.referenceDetail, name='reference-detail'),
]
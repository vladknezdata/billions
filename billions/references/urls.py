from django.urls import path
from . import views

app_name='references'

urlpatterns = [
    path('<slug:slug>', views.detail_view, name='detail_view'),
    path('', views.list_view, name='list_view')
]
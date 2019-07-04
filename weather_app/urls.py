from django.urls import path
from . import views


pk = []

urlpatterns = {
    path('', views.index, name = 'index'),
    path('delete/<int:id>', views.delete),
}

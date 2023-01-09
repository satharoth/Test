from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.inicio,name='inicio'),
    path('registarlibros/',views.registarlibros),
    path('edicionlibros/<ID>',views.edicionlibros),
    path('editarlibros/',views.editarlibros),
    path('eliminarlibros/<ID>',views.eliminarlibros)

]

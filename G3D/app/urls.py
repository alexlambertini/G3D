from django.urls import path
from .views import index
from . import views

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('enviar_mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
    path('load_more_images/', views.load_more_images, name='load_more_images'),
]

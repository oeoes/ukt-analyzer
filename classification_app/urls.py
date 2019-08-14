from django.urls import path
from . import views

app_name = 'classification_app'

urlpatterns = [
    path('', views.ukt_analyzer, name='ukt.analyzer'),
    path('predict', views.predict_ukt, name='predict.ukt')
]
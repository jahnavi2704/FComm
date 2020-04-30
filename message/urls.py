from django.urls import path, include
from . import views
urlpatterns = [
    path('select_topic/', views.main, name='message.main'),
    path('result/', views.result, name='message.result'),
    path('sent/', views.sent_messages, name='message.sent'),
    path('topic/', views.topic, name='message.topic'),
    path('topic_result/', views.topic_result, name='message.topic_result'),
    path('', views.select_topic, name='message.select_topic'),

]

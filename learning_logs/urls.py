"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]

from django.contrib import admin
from django.urls import path, re_path, include
from .views import PersonListView,PersonListAPIView,PersonView,PersonSearchAPIView

personas_patterns = [
    path('', PersonListView.as_view(), name='list'),
    path('api/lista', PersonListAPIView.as_view(), name='api_list'),
    path('list',PersonView.as_view(), name='list_ajax'),
    path(
        'api/search/<kword>/',
        PersonSearchAPIView.as_view(),
    )
]

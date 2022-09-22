from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('notes/',views.getNotes,name="getNotes"),
    path('notes/<str:pk>/update',views.updateNote,name="updateNote"),
    path('notes/<str:pk>/',views.getNote,name="getNote"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


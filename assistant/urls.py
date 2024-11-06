from django.urls import path
from .views import productivity_assistant_view

urlpatterns = [
    path("", productivity_assistant_view, name="productivity_assistant"),
]

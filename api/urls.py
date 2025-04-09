from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/interactions/",
        view=views.InteractionListCreateView.as_view(),
        name="list_or_create_interactions",
    )
]

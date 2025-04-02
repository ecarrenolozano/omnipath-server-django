from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/interactions/",
        views.list_or_create_interactions,
        name="list_or_create_interactions",
    ),
    path(
        "api/interactions/<int:pk>/",
        views.interaction_detail,
        name="interaction_detail",
    ),
    # path("api/stream/", views.stream_interactions, name="stream_interactions"),
]

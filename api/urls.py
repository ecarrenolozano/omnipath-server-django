from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^api/interactions$", views.interactions_list),
    re_path(r"^api/interactions/(?P<pk>[0-9]+)$", views.interaction_detail),
]

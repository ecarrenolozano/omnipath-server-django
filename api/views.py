import json

from django.http import StreamingHttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from api.models import Interactions
from api.serializers import InteractionsOmnipathSerializer


DEFAULT_INTERACTIONS_FIELDS = [
    "source",
    "target",
    "is_directed",
    "is_stimulation",
    "is_inhibition",
    "consensus_direction",
    "consensus_stimulation",
    "consensus_inhibition",
    "type",
]


# ----------------------------------------------------------------
# -------------------   INTERACTIONS  HANDLERS   -----------------
# ----------------------------------------------------------------
class InteractionListCreateView(APIView):
    """
    View for retrieving and creating interactions. Supports filtering and field selection.
    """

    @swagger_auto_schema(
        operation_description="Retrieve a list of interactions. Supports fields selection",
        manual_parameters=[
            openapi.Parameter(
                "dorothea_levels",
                openapi.IN_QUERY,
                description="Filter interactions by Dorothea levels",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "genesymbols",
                openapi.IN_QUERY,
                description="Filter interactions by genesymbols",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "fields",
                openapi.IN_QUERY,
                description="Comma-separated list of fields to return",
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: InteractionsOmnipathSerializer(many=True)},
    )
    def get(self, request):
        """
        Handles GET request for retrieving interactions with field selection.
        """
        queryset = Interactions.objects.all()

        # Get selected fields from query parameters
        selected_fields = request.query_params.get("fields")
        selected_fields = (
            selected_fields.split(",")
            if selected_fields
            else DEFAULT_INTERACTIONS_FIELDS
        )

        # Logic behind '?genesymbols'
        genesymbols_parameter = request.query_params.get("genesymbols")
        if genesymbols_parameter.lower() in {"1", "true"}:
            selected_fields.extend(("source_genesymbol", "target_genesymbol"))

        # Logic behind '?dorothea_levels'
        dorothea_levels_parameter = request.query_params.get("dorothea_levels")
        if dorothea_levels_parameter:
            queryset = queryset.filter(
                dorothea_level__icontains=dorothea_levels_parameter
            )
        print(dorothea_levels_parameter)

        # Serialize the queryset
        serializer = InteractionsOmnipathSerializer(
            queryset, many=True, fields=selected_fields
        )
        return JsonResponse(serializer.data, safe=False)


# ----------------------------------------------------------------------------------

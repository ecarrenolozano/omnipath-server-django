from django.http.response import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

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

    pagination_class = LimitOffsetPagination

    def paginate_queryset(self, queryset, request):
        paginator = self.pagination_class()
        return paginator.paginate_queryset(queryset, request, view=self)

    @swagger_auto_schema(
        operation_description="Retrieve a list of interactions. Supports fields selection",
        manual_parameters=[
            openapi.Parameter(
                "organisms",
                openapi.IN_QUERY,
                description="Filter interactions by ncbi_tad_id: 9606,10116,10090",
                type=openapi.TYPE_STRING,
            ),
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
        if selected_fields:
            selected_fields = DEFAULT_INTERACTIONS_FIELDS + selected_fields.split(",")
        else:
            DEFAULT_INTERACTIONS_FIELDS

        # Logic behind '?genesymbols'
        genesymbols_parameter = request.query_params.get("genesymbols")
        if (genesymbols_parameter is not None) and (genesymbols_parameter in {"1", "true"}):
            selected_fields.extend(("source_genesymbol", "target_genesymbol"))

        # Logic behind '?dorothea_levels'
        dorothea_levels_parameter = request.query_params.get("dorothea_levels")
        if dorothea_levels_parameter:
            print(dorothea_levels_parameter)
            queryset = queryset.filter(dorothea_level=dorothea_levels_parameter.split(","))

        # Logic behind ?organisms
        organisms_parameter = request.query_params.get("organisms")
        if organisms_parameter:
            print(organisms_parameter)
            queryset = queryset.filter(dorothea_level=dorothea_levels_parameter.split(","))

        print(queryset)
        print(selected_fields)

        paginated_qs = self.paginate_queryset(queryset, request)

        # Serialize the queryset
        serializer = InteractionsOmnipathSerializer(paginated_qs, many=True, fields=selected_fields)
        return JsonResponse(serializer.data, safe=False)


# ----------------------------------------------------------------------------------

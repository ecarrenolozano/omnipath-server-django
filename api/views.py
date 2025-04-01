from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import StreamingHttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Interactions
from api.serializers import InteractionsOmnipathSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET", "POST"])
def interactions_list(request):
    if request.method == "GET":
        interactions = Interactions.objects.all()  # Retrieve all objects

        source = request.GET.get("source", None)
        if source is not None:
            interactions = interactions.filter(source__icontains=source)

        interactions = interactions[:20]  #### Just for TESTING

        # serializing data before response
        interactions_omnipath_serializer = InteractionsOmnipathSerializer(
            interactions, many=True
        )
        return JsonResponse(interactions_omnipath_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "POST":
        interaction_data = JSONParser().parse(request)
        interactions_omnipath_serializer = InteractionsOmnipathSerializer(
            data=interaction_data
        )
        if interactions_omnipath_serializer.is_valid():
            interactions_omnipath_serializer.save()
            return JsonResponse(
                interactions_omnipath_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            interactions_omnipath_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def interaction_detail(request, pk):
    try:
        interaction = Interactions.objects.get(pk=pk)
    except Interactions.DoesNotExist:
        return JsonResponse(
            {"message": "The interaction does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        interactions_omnipath_serializer = InteractionsOmnipathSerializer(interaction)
        return JsonResponse(interactions_omnipath_serializer.data)

    elif request.method == "PUT":
        interactions_data = JSONParser().parse(request)
        interactions_omnipath_serializer = InteractionsOmnipathSerializer(
            interaction, data=interactions_data
        )
        if interactions_omnipath_serializer.is_valid():
            interactions_omnipath_serializer.save()
            return JsonResponse(interactions_omnipath_serializer.data)
        return JsonResponse(
            interactions_omnipath_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        interaction.delete()
        return JsonResponse(
            {"message": "Country was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def stream_interactions(request):
    """
    Streams the interactions data in JSON format instead of returning it all at once.
    This helps with large datasets.
    """
    source = request.GET.get("source", None)

    def data_generator():
        yield "["  # Start of JSON array
        first = True
        queryset = Interactions.objects.all()

        if source is not None:
            queryset = queryset.filter(source__icontains=source)

        for (
            obj
        ) in queryset.iterator():  # Uses an efficient iterator to fetch data in chunks
            if not first:
                yield ","
            first = False
            serialized_obj = InteractionsOmnipathSerializer(obj).data
            yield json.dumps(serialized_obj, cls=DjangoJSONEncoder)

        yield "]"  # End of JSON array

    response = StreamingHttpResponse(data_generator(), content_type="application/json")
    response["Content-Disposition"] = 'attachment; filename="interactions.json"'
    return response

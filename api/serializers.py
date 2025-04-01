from rest_framework import serializers
from api.models import Interactions


class InteractionsOmnipathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interactions
        fields = (
            "id",
            "source",
            "target",
            "source_genesymbol",
            "target_genesymbol",
            "is_directed",
            "is_stimulation",
            "is_inhibition",
            "consensus_direction",
            "consensus_stimulation",
            "consensus_inhibition",
            "sources",
            "references",
            "omnipath",
            "kinaseextra",
            "ligrecextra",
            "pathwayextra",
            "mirnatarget",
            "dorothea",
            "collectri",
            "tf_target",
            "lncrna_mrna",
            "tf_mirna",
            "small_molecule",
            "dorothea_curated",
            "dorothea_chipseq",
            "dorothea_tfbs",
            "dorothea_coexp",
            "dorothea_level",
            "type",
            "curation_effort",
            "extra_attrs",
            "evidences",
            "ncbi_tax_id_source",
            "entity_type_source",
            "ncbi_tax_id_target",
            "entity_type_target",
        )  # Here we define the field to return in the response

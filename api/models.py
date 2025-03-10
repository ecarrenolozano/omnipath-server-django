from django.db import models
from django.contrib.postgres.fields import ArrayField


# Model for the table `interactions_omnipath`.
class InteractionsOmnipath(models.Model):
    source = models.CharField(null=True, blank=True)
    target = models.CharField(null=True, blank=True)
    source_genesymbol = models.CharField(null=False, blank=True)
    target_genesymbol = models.CharField(null=False, blank=True)
    is_directed = models.BooleanField()
    is_stimulation = models.BooleanField()
    is_inhibition = models.BooleanField()
    consensus_direction = models.BooleanField()
    consensus_stimulation = models.BooleanField()
    consensus_inhibition = models.BooleanField()
    sources = ArrayField(models.CharField(max_length=255))
    references = models.CharField(null=False, blank=True)
    omnipath = models.BooleanField()
    kinaseextra = models.BooleanField()
    ligrecextra = models.BooleanField()
    pathwayextra = models.BooleanField()
    mirnatarget = models.BooleanField()
    dorothea = models.BooleanField()
    collectri = models.BooleanField()
    tf_target = models.BooleanField()
    lncrna_mrna = models.BooleanField()
    tf_mirna = models.BooleanField()
    small_molecule = models.BooleanField()
    dorothea_curated = models.BooleanField()
    dorothea_chipseq = models.BooleanField()
    dorothea_tfbs = models.BooleanField()
    dorothea_coexp = models.BooleanField()
    dorothea_level = ArrayField(models.CharField(max_length=255))
    type = models.CharField(null=False, blank=True)
    curation_effort = models.IntegerField()
    extra_attrs = models.JSONField(null=True, blank=True)
    evidences = models.JSONField(null=True, blank=True)
    ncbi_tax_id_source = models.IntegerField()
    entity_type_source = models.CharField(null=False, blank=True)
    ncbi_tax_id_target = models.IntegerField()
    entity_type_target = models.CharField(null=False, blank=True)

    class Meta:
        db_table = "interactions_omnipath"  # Name of the table in the database
        verbose_name = (
            "Interactions Omnipath"  # Optional, for human-readable name in Django admin
        )
        ordering = ("id",)

    def __str__(self):
        return f"({self.name}, {self.capital})"

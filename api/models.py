from django.db import models
from django.contrib.postgres.fields import ArrayField


# Model for the table `interactions`.
class Interactions(models.Model):
    source = models.CharField(null=True, blank=True)
    target = models.CharField(null=True, blank=True)
    source_genesymbol = models.CharField(null=False, blank=True)
    target_genesymbol = models.CharField(null=False, blank=True)
    is_directed = models.BooleanField(null=True, blank=True)
    is_stimulation = models.BooleanField(null=True, blank=True)
    is_inhibition = models.BooleanField(null=True, blank=True)
    consensus_direction = models.BooleanField(null=True, blank=True)
    consensus_stimulation = models.BooleanField(null=True, blank=True)
    consensus_inhibition = models.BooleanField(null=True, blank=True)
    sources = ArrayField(models.CharField(max_length=255), null=True)
    references = models.CharField(null=True, blank=True)
    omnipath = models.BooleanField(null=True, blank=True)
    kinaseextra = models.BooleanField(null=True, blank=True)
    ligrecextra = models.BooleanField(null=True, blank=True)
    pathwayextra = models.BooleanField(null=True, blank=True)
    mirnatarget = models.BooleanField(null=True, blank=True)
    dorothea = models.BooleanField(null=True, blank=True)
    collectri = models.BooleanField(null=True, blank=True)
    tf_target = models.BooleanField(null=True, blank=True)
    lncrna_mrna = models.BooleanField(null=True, blank=True)
    tf_mirna = models.BooleanField(null=True, blank=True)
    small_molecule = models.BooleanField(null=True, blank=True)
    dorothea_curated = models.BooleanField(null=True, blank=True)
    dorothea_chipseq = models.BooleanField(null=True, blank=True)
    dorothea_tfbs = models.BooleanField(null=True, blank=True)
    dorothea_coexp = models.BooleanField(null=True, blank=True)
    dorothea_level = ArrayField(models.CharField(max_length=255), null=True)
    type = models.CharField(null=True, blank=True)
    curation_effort = models.IntegerField(null=True)
    extra_attrs = models.JSONField(null=True, blank=True)
    evidences = models.JSONField(null=True, blank=True)
    ncbi_tax_id_source = models.IntegerField(null=True)
    entity_type_source = models.CharField(null=True, blank=True)
    ncbi_tax_id_target = models.IntegerField(null=True)
    entity_type_target = models.CharField(null=True, blank=True)

    class Meta:
        db_table = "interactions"  # Name of the table in the database
        ordering = ("id",)

    def __str__(self):
        return f"({self.source}, {self.target}, {self.id}, {self.source_genesymbol})"

import uuid

from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class GeoProBaseModel(TimeStampedModel, SoftDeletableModel):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

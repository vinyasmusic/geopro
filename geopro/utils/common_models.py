import uuid

from django.db import models
from model_utils.models import TimeStampedModel


class GeoProBaseModel(TimeStampedModel):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

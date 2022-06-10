from django.db import models
import uuid
from model_utils.models import TimeStampedModel, SoftDeletableModel


class GeoProBaseModel(TimeStampedModel, SoftDeletableModel):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

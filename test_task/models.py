from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField

# Create your models here.
class TestModel(models.Model):
    data = JSONField()

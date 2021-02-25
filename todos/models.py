from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, default='', null=True)
    # items są przechowywane jako json listy, dzięki takiemu podejściu to front decyduje jakiego typu dane chcemy prezentować, edytować itd.
    # daje nam to elastyczność na froncie
    items = models.TextField(default='[]')

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False)
    type_id = models.UUIDField(null=True)
    block = models.CharField(null=True)
    auto_updates = models.BooleanField(default=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']


class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    eoNumber = models.CharField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to="docs")

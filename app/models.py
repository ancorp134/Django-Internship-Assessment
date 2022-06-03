import email
from django.db import models
from pkg_resources import require
import uuid

class Record(models.Model):
    id=models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id + self.created_at

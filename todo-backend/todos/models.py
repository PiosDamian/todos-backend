from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}: {self.name} [{self.done}]'

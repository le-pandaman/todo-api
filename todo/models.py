from django.db import models

# Create your models here.


class Todo(models.Model):

    task = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    completed = models.DateField()

    def __str__(self) -> str:

        return self.task

    def __repr__(self) -> str:

        return self.task

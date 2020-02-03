from django.db import models

# Create your models here.
class Todo(models.Model):

    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name+" - "+str(self.done)
    
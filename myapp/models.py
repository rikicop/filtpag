from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(default=5)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

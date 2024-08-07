from django.db import models


class Column(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.title
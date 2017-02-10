from django.db import models
from datetime import datetime

class Comment(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="parent_comment", null=True)
    children = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children_comment", null=True)
    time = models.DateTimeField()
    comment = models.CharField(max_length=500)
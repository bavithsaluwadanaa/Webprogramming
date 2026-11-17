from django.db import models

class HashRecord(models.Model):
    text = models.TextField()
    digest = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.digest

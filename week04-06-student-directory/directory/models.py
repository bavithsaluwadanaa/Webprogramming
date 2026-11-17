from django.db import models

class Module(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    def __str__(self): return f"{self.code} — {self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(unique=True)
    enrolment_date = models.DateField()
    modules = models.ManyToManyField(Module, related_name="students", blank=True)
    image = models.ImageField(upload_to="students/", blank=True)
    def __str__(self): return f"{self.first_name} {self.last_name}"
    class Meta:
        ordering = ["last_name", "first_name"]

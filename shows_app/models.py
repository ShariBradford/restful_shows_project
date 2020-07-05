from django.db import models

# Create your models here.
class Network(models.Model):
    # id INT
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f"<Network object: {self.name} ({self.id})>"

class Show(models.Model):
    # id INT
    title = models.CharField(max_length=255)
    desc = models.TextField()
    network = models.ManyToManyField(Network,related_name="shows")
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f"<Show object: {self.title} ({self.id})>"





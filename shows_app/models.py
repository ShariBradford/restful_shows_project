from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if not postData['show_title']:
            errors['show_title'] = "Title is required."
        elif len(postData['show_title']) < 2:
            errors['show_title'] = "Title should be at least 2 characters."

        if not postData['show_network']:
            errors['show_network'] = "Network is required."
        elif len(postData['show_network']) < 3:
            errors['show_network'] = "Network should be at least 3 characters."

        if postData['show_description'] and len(postData['show_description']) < 10:
            errors['show_description'] = "If provided, description should be at least 10 characters."
        
        if not postData['release_date']:
            errors['release_date'] = "Release date is required."
        elif datetime.strptime(postData['release_date'],'%Y-%m-%d') > datetime.today():
            errors['release_date'] = "Release date must be in the past."

        return errors


class Show(models.Model):
    # id INT
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    network = models.CharField(max_length=20)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Show object: {self.title} ({self.id})>"





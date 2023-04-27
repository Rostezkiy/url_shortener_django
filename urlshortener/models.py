from django.db import models
from .utils import create_shortened_url


# Create your models here.

class Shortener(models.Model):
    """
    Creates a short url based on the long one
    Fields:
    created - Time when shortener was created
    times_followed - Amount of times shortened link has been followed
    long_url - The original link
    short_url -  Shortened link https://domain/(short_url)
    """
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.short_url:
            # Pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

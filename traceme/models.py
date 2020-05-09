from django.db import models
from django.contrib.auth.models import User

# Place model - stores a place
class Place(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user")
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
    start = models.CharField(max_length=24)
    end = models.CharField(max_length=24, blank=True, null=True)
    reason = models.CharField(max_length=64)
    event = models.CharField(max_length=64, blank=True, null=True)

    # Return basic information about place
    def __str__(self):
        return f"{self.city}, {self.country}. User: {self.user.username}"

    # Return JSON summary of place
    def getinfo(self):
        placeinfo = {
            "user": self.user.username,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start": str(self.start),
            "end": str(self.end),
            "reason": self.reason,
            "event": self.event,
        }

        return placeinfo

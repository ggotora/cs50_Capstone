from django.db import models
from main.models import Profile
from django.utils import timezone
from django.urls import reverse
import datetime
from django.db.models.signals import post_save


class Location(models.Model):
    address_1 = models.CharField(max_length=200, null=True, blank=True)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100, default='Zimbabwe')

    def get_absolute_url(self):
        return reverse("loads:location_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        if self.address_1:
            return f"{self.address_1[:17]}...{self.city}"
        return f"{self.city}"


class Load(models.Model):
    class Type (models.TextChoices):
        REFEER = "R", ("Reefer")
        FLATBED = "F", ("Flatbed")
        SIDE_CURTAIN = "S", ("Side Curtain")
        OTHER = "O", ("Other")
        VAN = "V", ("Van")
    origin = models.ForeignKey(Location, related_name='outgoing', on_delete=models.CASCADE)
    destination = models.ForeignKey(Location, related_name='incoming', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=Type.choices, default=Type.FLATBED)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    weight = models.CharField(max_length=20)
    rate = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.origin} to {self.destination}"
    
    def get_absolute_url(self):
        return reverse("loads:load", kwargs={"pk": self.pk})
    
    
    
class LoadStatus(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "A", ("Available")
        IN_TRANSIT = "I", ("In Transit")
        DELIVERED = "D", ("Delivered")
    
    load = models.OneToOneField(Load, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.AVAILABLE)
    transporter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_status_display()}"
    
    def pub_within_24(self):
        return timezone.now() - self.updated <=  datetime.timedelta(hours=24)
    

def create_load(sender, created,instance,  *args, **kwargs):
    if created:
        LoadStatus.objects.create(load=instance, transporter=instance.owner)

post_save.connect(create_load, sender=Load)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.urls import reverse

class User(AbstractUser):
    pass 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    organisation = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) 
    # email = models.EmailField(max_length=254)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    created = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_absolute_url(self):
        return reverse("main:profile", kwargs={"pk": self.pk})
    

def create_user_profile(sender, created,instance,  *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class clothes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    image = models.ImageField(upload_to='media')
    cloth_name = models.CharField(max_length=100, null=True)
    fashion_name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    

    def __str__(self):
        return self.cloth_name or "Unnamed Cloth"

class Message(models.Model):
    name=models.CharField(null=True,max_length=50)
    email=models.EmailField(null=True,unique=True, max_length=254)
    subject=models.CharField(null=True, max_length=50)
    message=models.TextField(null=True)

class Profile(models.Model):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class order(models.Model):
    relation=models.ForeignKey(clothes, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)
    cloth_name=models.CharField(null=True)
    size=models.CharField( max_length=50)
    email=models.EmailField(max_length=254,null=True)
    phone=models.CharField(null=True)
    address=models.TextField(null=False)
    def __str__(self):
        return self.cloth_name
    


class CustomerReview(models.Model):
    khan = models.ForeignKey(clothes, on_delete=models.CASCADE, null=True, blank=True)
  
    info = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.info
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    gender = (
        ("Man","Мужчина"),
        ("Woman","Женщина"),
    )

    user = models.OneToOneField(get_user_model(), verbose_name="Пользователь", on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="Пол", max_length=50, blank=True, null=True)
    

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


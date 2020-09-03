from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    #Sort of like inheriting from User but not really, it's kind of like extending the class
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #addtional
    #They don't have to fill it out
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank = True)

    def __str__(self):
        return self.user.username

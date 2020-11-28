from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE) #Add exta attributes to each User


    # additional
    portfolio_site=models.URLField(blank=True) # Means it's optional



    profile_pic=models.ImageField(upload_to='profile_pics',blank=True) #Users' picture will be uploaded to media/profile_pics directory


    def __str__(self):
        return self.user.username
